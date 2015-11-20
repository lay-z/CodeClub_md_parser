import os
import json

import config
import project_finder
import database_writer

environment = os.environ.get('PYTHON_ENV','development')
mongolabUri = 'mongodb://localhost:27017/turing_development'

if (environment == 'production'):
    mongolabUri = config.mongolabUri

projects = []
for project in project_finder.find_projects():
    if (project['title'] not in config.projects['ignore']):
        projects.append(project)

json.dump(open('data/projects_codeclub.json','w'),projects)
databaseWriter = database_writer.DatabaseWriter('projects',mongolabUri)

print('Updating {} Database'.format(environment.title()))
print('='*80)

for project in projects:
    updated = databaseWriter.update({ 'title' : project['title'] },project)
    print(updated.get('title',''),updated.get('link',''))