# vim: fileencoding=utf-8
from __future__ import print_function, absolute_import, unicode_literals

from argparse import ArgumentParser
import codecs
try:
    import configparser
    _CONFIG_PARSER = configparser.ConfigParser
except ImportError:
    import ConfigParser as configparser
    _CONFIG_PARSER = configparser.SafeConfigParser
import os
import sys
import tarfile
import tempfile


class Provisioner(object):
    PROG = 'make_provisioner'
    config = None
    options = None

    def get_sfx_stub(self):
        txt = get_data('scripts/guest.sh').decode('utf-8')

        # I would check that RUNNER would not be '../../pwnx0r', but the
        # provisioner could just be "exec /var/pwnx0r" instead.  Without this.
        conf = self.config
        d = {"CUT_LINE": 1 + txt.count("\n"),
             "CLOUD_DIR": shquote(conf.get("guest_stage2_dir", "/var/tmp/cloud-maker")),
             "RUNNER": shquote('./' + conf.get("stage2_script", "main.sh")),
            }

        if d is None:
            raise Exception("Demo exception thrown")

        return Template(txt).substitute(d)

    def read_config(self, system, path, encoding='utf-8'):
        default = configparser.DEFAULTSECT
        ini = _CONFIG_PARSER() # ConfigParser [py3] or SafeConfigParser [py2]
        ini.optionxform = lambda o: o
        with codecs.open(path, 'r', encoding=encoding) as fp:
            try:
                ini.read_file(fp, path)
            except AttributeError:
                ini.readfp(fp, path)

        # set defaults from the environment
        if not ini.has_option(default, 'HOME'):
            ini.set(default, 'HOME', os.path.expanduser("~"))
        if not ini.has_option(default, 'USER'):
            ini.set(default, 'USER', _first_key(os.environ, ("USER", "USERNAME", "LOGNAME"), ''))
        if not ini.has_option(default, 'INI_DIR'):
            ini.set(default, 'INI_DIR', os.path.abspath(os.path.dirname(path)))

        # make a dictionary interface to the config because I like it.
        # the difference: this version resolves HOME/USER now, not later.
        # so if you're extending this, beware of that, I guess :-/
        self.config = dict(ini.items(system))

    def build_tar(self, fp, rootdir):
        # If we're not on Windows, rely on the host's executable bits.
        # Otherwise, split off for a massive hack.
        tar = tarfile.open(mode='w:gz', fileobj=fp, compresslevel=9)
        try:
            if platform.system() == 'Windows':
                self._build_tar_win(fp, rootdir, tar)
            else:
                self._build_tar_posix(fp, rootdir, tar)
        finally:
            tar.close()
