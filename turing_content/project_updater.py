import os
import glob
import json
import http.server

import config
import project_object
import language_object
import database_writer
import directory_watcher
import resource_uploader

class Resource:
    pass

def findProjects():
    """Find all projects in the given folder
    """

    # Create a list to collect projects
    projects = json.load(open('data/projects_codeclub.json'))
    filenames = glob.glob('projects/**/*.json')

    # For all project files 
    for filename in filenames:

        # Access the project
        try:
            project = json.load(open(filename))
        except Exception as error:
            print('='*35,'  ERROR  ','='*35)
            print(filename)
            print(error)
            print('='*80)
            continue 

        # Add to list of projects
        projects.append(project)

    return projects
    
def findResources():
    """Find all resources in resources folder
    """

    resources = []

    root = 'resources/'
    filenames = glob.glob(root + '**/*.*', recursive=True)

    for filename in filenames:

        if (root not in filename):
            print('Error {} does not contain {}'.format(filename,root))
            continue

        resource = Resource()
        resource.localFilePath = filename
        resource.awsFilePath = filename[len(root):]
        resources.append(resource)

    return resources

def update():

    environment = os.environ.get('PYTHON_ENV','development')
    print('Updating {} Database'.format(environment.title()),'\n','='*80)

    mongolabUri = config.mongolabUri[environment]
    
    # Update languages
    languages = database_writer.DatabaseWriter('languages',mongolabUri)
    for _language in json.load(open('data/languages.json')):
        language = language_object.Language(languages)
        language.load(_language)
        language.format(config.turingResources[environment])
        language.save()

    # Update projects
    projects = database_writer.DatabaseWriter('projects',mongolabUri)
    overview = json.load(open('data/overview.json'))
    for _project in findProjects():

        # Check if project exists in overview
        if (_project['title'] in overview):
            print(_project['title'])
        else:
            print('\t',_project['title'],'not found in overview')
            continue

        project = project_object.Project(projects)
        project.load(_project)
        project.update(overview[_project['title']])
        project.format(config.turingResources[environment])
        project.save(environment)

def main():

    update()
    environment = os.environ.get('PYTHON_ENV','development')

    if (environment == 'development'):

        # Create a server function
        def server():
            http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler,port=config.port)

        # Watch the directory for changed
        directory_watcher.eventLoop(update,server)

    elif (environment == 'production'):

        # Construct the resource uploader
        uploader = resource_uploader.ResourceUploader()
        uploader.setBucket(config.bucketName)

        # Find all the resources in the resources folder
        resources = findResources()
        print('Uploading {} files to \'{}\''.format(len(resources),config.bucketName),'\n','='*80)

        # For all resources found upload to s3
        for i,resource in enumerate(resources):
            uploader.uploadFile(resource.awsFilePath,resource.localFilePath)
            if (i%10 == 0): print('{}/{}'.format(i,len(resources)))

        print('Upload Complete')

    else:
        raise RuntimeError(
            'PYTHON_ENV must be production or development not {}'.format(
                environment
                )
            )


if (__name__ == "__main__"):
    main()