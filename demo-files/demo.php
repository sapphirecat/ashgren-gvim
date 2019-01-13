<?php
namespace sapphirecat\colorscheme;
use Aws\S3\S3Client;

class DemoClass
{
    /** @var string $question Some doc comment */
    protected $question = "the meaning of life, the universe, and everything";
    protected $answer = 42;

    public function shoutQuestion(): void
    {
        echo strtoupper($this->question), PHP_EOL;
    }

    /** Contrived example.
     *
     * @param S3Client $s3 The AWS SDK client
     * @param string $bucket Bucket name to upload to
     * @param string[] $files List of full paths to files to upload
     * @return int Count of successfully uploaded files
     */
    protected function uploadFileList(S3Client $s3, string $bucket, array $files): int
    {
        $ok = 0;
        foreach ($files as $file) {
            try {
                $s3->putObject(['Bucket' => $bucket, 'Key' => basename($file)]);
                ++$ok;
            } catch (Exception $ex) {
                error_log("$file: {$ex->getMessage()}");
            }
        }
        return $ok;
    }
}

