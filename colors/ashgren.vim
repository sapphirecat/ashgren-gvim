" Author: sapphirecat <devel@sapphirepaw.org>

highlight clear
if exists("syntax_on")
    syntax reset
endif

let g:colors_name = 'ashgren'
set background=light

" basics
hi Normal       gui=NONE    guifg=#000000   guibg=#b5b5a9
hi Visual                                   guibg=#c9c9bd

" syntax elements
hi Comment      gui=NONE    guifg=#745879
hi Constant     gui=NONE    guifg=#a00069
hi Error        gui=NONE    guifg=#fafafa   guibg=#970019
hi Identifier   gui=NONE    guifg=#00887b
hi PreProc      gui=NONE    guifg=#0053aa
hi Special      gui=NONE    guifg=#970019
hi Statement    gui=bold    guifg=#917100
hi Title        gui=bold    guifg=#ce398b
hi Type         gui=NONE    guifg=#008f2b
hi Underlined   gui=underline guifg=#0053aa

" gvim interface
hi LineNr       gui=NONE    guifg=#3f2b38   guibg=#abab9f
hi CursorLineNR gui=bold    guifg=#3f2b38   guibg=#97988c
hi CursorLine                               guibg=#9f9f94
hi CursorColumn                             guibg=#9f9f94
hi ColorColumn                              guibg=#b0a0a2

hi StatusLine   gui=bold    guifg=#fafafa   guibg=#745879
hi StatusLineNC gui=NONE    guifg=#4a4a4a   guibg=#b9aabc
hi VertSplit    gui=NONE    guifg=#4a4a4a   guibg=#b9aabc

hi SpecialKey   gui=bold    guifg=#3f2b38
hi NonText      gui=NONE    guifg=#8a8a8a
hi ErrorMsg     gui=NONE    guifg=#fafafa   guibg=#f21d22
hi WarningMsg   gui=bold    guifg=#970019
hi Search                                   guibg=#ffdd62
hi Todo         gui=bold    guifg=#0053aa   guibg=#ffdd62

hi Pmenu        gui=NONE    guifg=#4a4a4a   guibg=#95c091
hi PmenuSel     gui=bold    guifg=#4a4a4a   guibg=#aff7ab
hi PmenuSbar                                guibg=#cacaca
hi PmenuThumb                               guibg=#374436

" plugin tweaks
hi GitGutterChangeDefault   guifg=#ffdd62

" vim:sts=4:sw=4:et