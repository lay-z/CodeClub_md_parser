import os
import json
import http.server

import config
import project_finder
import database_writer

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