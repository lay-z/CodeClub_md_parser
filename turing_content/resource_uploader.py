import os
import pytz
import time
import datetime
import logging
import boto3

import config

boto3.set_stream_logger('boto3.resources', logging.WARNING)

def exists(key):
    exists = False

    try:
        key.load()
    except Exception as error:
        if (error.response['Error']['Code'] == "404"):
            exists = False
        else:
            raise error
    else:
        exists = True

    return exists

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

        
        # Construct amazon bucket and check last modified
        key = self.s3.Object(self.bucketName, awsFilePath)

        # Check if key exists and return
        if (exists(key)):
            return
        
        # Print the file is updating
        print('Updating {}'.format(localFilePath))
        key.put(ACL='public-read',Body=open(localFilePath, 'rb'))


if (__name__ == "__main__"):

    resourceUploader = ResourceUploader()
    resourceUploader.setBucket('turing-resources')
    resourceUploader.uploadFile('temp/test.txt','resources/test.txt')


