import boto

class ResourceUploader:

    def __init__(self,s3Connection):
        """Contruct the resource uploader class with a instanciated s3
        connection
        """

        self.s3Connection = s3Connection


    def setBucket(self,bucketName):
        """Set the bucket using the s3 connection and bucket name

        @params:
            bucketName - name of aws bucket
        """

        self.bucket = self.s3Connection.get_bucket(bucketName)


    def uploadFile(self,filePath,fileObject):
        """Upload a given file to the amazon s3 bucket

        @params
            filePath - path to file in amazon s3
            fileObject - opened file object to be uploaded to s3
        """

        key = boto.s3.key.Key(self.bucket, filePath)
        key.send_file(fileObject)
        fileObject.close()


if (__name__ == "__main__"):

    import config

    resourceUploader = ResourceUploader(
        boto.connect_s3(
            config.aws['accessKeyId'],
            config.aws['secretAccessKey']
            )
        )
    resourceUploader.setBucket('turing-resources')
    resourceUploader.uploadFile('temp/test.txt',open('resources/test.txt'))


