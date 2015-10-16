import os
import glob
import json
import sections

amazonUrl = 'https://s3-eu-west-1.amazonaws.com/turing-resources/'

def changeImagePath(dictionary,rootUrl):
	"""Recusrively look into dictionary to chagne the image keys to prepend a root url
	"""

	if (type(dictionary) is not dict):
		return

	for key in dictionary:
		if ((key == 'image') and (dictionary[key] is not None)):
			print(key,dictionary[key],dictionary)
			dictionary[key] = rootUrl + dictionary[key]
		elif (type(dictionary[key]) == dict):
			changeImagePath(dictionary[key],rootUrl)
		elif (type(dictionary[key]) == list):
			for item in dictionary[key]:
				changeImagePath(item,rootUrl)

# Create a list to collect projects
projects = []

# Find all md files in code_club fodler
markdownFiles = glob.glob('code_club/**/*.md')
for markdownFile in markdownFiles:

	# Check if notes in file
	if ('- notes' in markdownFile):
		continue

	# Access the data
	with open(markdownFile) as openFile:
		data = sections.split_project(openFile.read())

	# Change all image references to include full source
	rootUrl = amazonUrl + os.path.split(os.path.split(markdownFile)[0])[1]
	changeImagePath(data,rootUrl)

	# Add project data to a list
	projects.append(data)

with open('projects.json','w') as openFile:
	json.dump(projects,openFile,indent=4)