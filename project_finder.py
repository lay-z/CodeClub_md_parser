import os
import re
import glob
import json

import notes_parser
import project_parser

amazonUrl = 'https://s3-eu-west-1.amazonaws.com/turing-resources/'

def changeImagePath(dictionary,rootUrl):
    """Recusrively look into dictionary to chagne the image keys to prepend a root url
    """

    if (type(dictionary) is not dict):
        return

    for key in dictionary:
        if ((key == 'image') and (dictionary[key] is not None)):
            # print(key,dictionary[key],dictionary)
            dictionary[key] = "{}/{}".format(rootUrl,dictionary[key])
        elif (type(dictionary[key]) == dict):
            changeImagePath(dictionary[key],rootUrl)
        elif (type(dictionary[key]) == list):
            for item in dictionary[key]:
                changeImagePath(item,rootUrl)

# Create a list to collect projects
projects = {}

# Find all md files in code_club fodler
markdownFiles = glob.glob('code_club/**/*.md')
for markdownFile in markdownFiles:

    # Access the data
    folder = os.path.split(os.path.split(markdownFile)[0])[1]
    project = projects.get(folder,{})

    # Open the markdown file
    with open(markdownFile) as openFile:
        fileContent = openFile.read()

    # Check if notes in file
    if ('- notes' in markdownFile):
        data = notes_parser.parse_notes(fileContent)
    else:
        data = project_parser.parse_project(fileContent)

        # Change all image references to include full source
        rootUrl = amazonUrl + folder
        changeImagePath(data,rootUrl)

    project.update(data)
    projects[folder] = project


with open('projects.json','w') as openFile:
    json.dump(list(projects.values()),openFile,indent=4)