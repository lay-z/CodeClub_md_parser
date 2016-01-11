import os
import glob
import json
import http.server

import config
import project_object
import database_writer


def findProjects():
    """Find all projects in the given folder
    """

    # Create a list to collect projects
    projects = json.load(open('data/projects_codeclub.json'))
    filenames = glob.glob('projects/*.json')

    # For all project files 
    for filename in filenames:

        # Access the project
        project = json.load(open(filename))

        # Add to list of projects
        projects.append(project)

    return projects
    

def main():
    environment = os.environ.get('PYTHON_ENV','development')
    print('Updating {} Database'.format(environment.title()),'\n','='*80)

    mongolabUri = config.mongolabUri[environment]
    collection = database_writer.DatabaseWriter('projects',mongolabUri)

    overview = json.load(open('data/overview.json'))

    for _project in findProjects():

        # Check if project exists in overview
        if (_project['title'] in overview):
            print(_project['title'])
        else:
            print('\t',_project['title'],'not found in overview')
            continue

        project = project_object.Project(collection)
        project.load(_project)
        project.update(overview[_project['title']])
        project.format(config.turingResources[environment])
        project.save()

    if (environment == 'development'):
        http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler,port=config.port)

if (__name__ == "__main__"):
    main()