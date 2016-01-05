import os
import json

import config
import project_finder
import database_writer

def main():
    environment = os.environ.get('PYTHON_ENV','development')
    mongolabUri = 'mongodb://localhost:27017/turing_development'

    if (environment == 'production'):
        mongolabUri = config.mongolabUri

    databaseWriter = database_writer.DatabaseWriter('projects',mongolabUri)

    print('Updating {} Database'.format(environment.title()))
    print('='*80)

    for project in project_finder.find_projects():

        if (project['name'] not in config.projects):
            print('  -  {title}'.format(**project))
            continue

        updated = databaseWriter.update({ 'number' : project['number'] },project)
        print('{title}'.format(**updated))

if (__name__ == "__main__"):
    main()