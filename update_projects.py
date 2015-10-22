import config
import project_finder
import database_writer

DEVELOPMENT = True

if (DEVELOPMENT):
		mongolabUri = 'mongodb://localhost:27017/turing_development'
else:
		mongolabUri = config.mongolabUri

projects = project_finder.find_projects()
databaseWriter = database_writer.DatabaseWriter('projects',config.mongolabUri)

for project in projects:
		print('---',project.get('link',''))
		print(databaseWriter.update({ 'title' : project['title'] },project))

for project in databaseWriter.query():
		print('hello')
		print(project.get('link',''))