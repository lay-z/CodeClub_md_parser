import boto3
import config

class ResourceUploader:

    def __init__(self,session=boto3.session.Session(**config.aws)):
        """Contruct the resource uploader class with a instanciated s3
        connection
        """

        self.s3 = session.resource('s3')


    def setBucket(self,bucketName):
        """Set the aws bucket being uploaded to

        @params
            bucketName - name of aws bucket    
        """

        self.bucketName = bucketName

    def uploadFile(self,awsFilePath,localFilePath):
        """Upload a given file to the amazon s3 bucket

        @params
            filePath - path to file in amazon s3
            fileObject - opened file object to be uploaded to s3
        """

        key = self.s3.Object(self.bucketName, awsFilePath)
        key.put(Body=open(localFilePath, 'rb'))
        key.put(ACL='public-read')


if (__name__ == "__main__"):

    resourceUploader = ResourceUploader()
    resourceUploader.setBucket('turing-resources')
    resourceUploader.uploadFile('temp/test.txt','resources/test.txt')


