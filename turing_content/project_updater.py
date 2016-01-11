import os
import json
import http.server

import config
import project_finder
import database_writer


def find_projects(environment):
    """Find all projects in the given folder
    """

    # Create a list to collect projects
    projects = []
    projectFilenames = glob.glob('projects/*.json')

    # For all project files 
    for projectFilename in projectFilenames:

        # Access the project
        project = json.load(open(projectFilename))

        # Change all image references to include full source
        change_image_path(project,config.imageRoot[environment])

        # Add to list of projects
        projects.append(project)

    return projects
    

def main():
    environment = os.environ.get('PYTHON_ENV','development')
    mongolabUri = config.mongolabUri[environment]

    databaseWriter = database_writer.DatabaseWriter('projects',mongolabUri)

    print('Updating {} Database'.format(environment.title()))
    print('='*80)

    for project in project_finder.find_projects(environment):

        if (project['name'] not in config.projects[environment]):
            print('  -  {title}'.format(**project))
            continue

        updated = databaseWriter.update({ 'number' : project['number'] },project)
        print('{title}'.format(**updated))

    if (environment == 'development'):
        http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler,port=config.port)

if (__name__ == "__main__"):
    main()