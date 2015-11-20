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

    codeclubProjects = []
    for project in project_finder.find_projects():
        if (project['title'] not in config.projects['ignore']):
            codeclubProjects.append(project)

    json.dump(codeclubProjects,open('data/projects_codeclub.json','w'),indent=4)
    turinglabProjects = json.load(open('data/projects_turinglab.json'))
    projects = turinglabProjects + codeclubProjects

    corrections = json.load(open('data/corrections.json'))
    for project in projects:
        projectCorrections = corrections[project['title']]

        for correction in projectCorrections:
            exec('project' + correction, globals(), {'project':project})


    json.dump(projects,open('data/projects.json','w'),indent=4)
    databaseWriter = database_writer.DatabaseWriter('projects',mongolabUri)

    print('Updating {} Database'.format(environment.title()))
    print('='*80)

    for project in projects:
        updated = databaseWriter.update({ 'title' : project['title'] },project)
        print(updated.get('title',''),updated.get('link',''))

if (__name__ == "__main__"):
    main()