import os
import re
import glob
import json
import urllib.parse

import config
import notes_parser
import project_parser

def build_root_url(url,directory,filename):
    """Build a root url from the base url and a directory
    """

    path = '{}/{}'.format(directory,filename)
    path = urllib.parse.quote(path)
    return url + path 


def change_image_path(dictionary,rootUrl):
    """Recusrively look into dictionary to chagne the image keys to prepend a root url
    """

    if (type(dictionary) is not dict):
        return

    for key in dictionary:
        if ((key == 'image') and (dictionary[key] is not None)):
            # print(key,dictionary[key],dictionary)
            dictionary[key] = "{}/{}".format(rootUrl,dictionary[key])
        elif (type(dictionary[key]) == dict):
            change_image_path(dictionary[key],rootUrl)
        elif (type(dictionary[key]) == list):
            for item in dictionary[key]:
                change_image_path(item,rootUrl)


def find_markdown(root,language,folders):
    """Find all markdown files given the 
    """

    results = []
    for folder in folders:
        expression = '{}/{}/{}/**/*.md'.format(root,language,folder)
        matches = glob.glob(expression)
        results.extend(matches)

    return results

def find_projects():
    """Find all projects in the given folder
    """

    # Create a list to collect projects
    projects = {}

    # Find all md files in code_club fodler
    markdownFiles = find_markdown(
        config.codeClub['root'],
        config.codeClub['language'],
        config.codeClub['folders']
        )

    # For all markdown files create a project
    for markdownFile in markdownFiles:

        # Access the data
        print(markdownFile)
        projectName = os.path.split(os.path.split(markdownFile)[0])[1]
        project = projects.get(projectName,{'name':projectName})

        # Open the markdown file
        with open(markdownFile) as openFile:
            fileContent = openFile.read()

        # If notes file use notes parser to extract information
        if ('- notes' in markdownFile):
            data = notes_parser.parse_notes(fileContent)

        # Otherwise use project parser to extract information
        else:
            data = project_parser.parse_project(fileContent)

            # Change all image references to include full source
            rootUrl = config.imageUrl + projectName
            change_image_path(data,rootUrl)

        # Combine data with existing project data
        project.update(data)
        projects[projectName] = project

    return projects

if (__name__ == "__main__"):

    projects = find_projects()

    with open('projects.json','w') as openFile:
        json.dump(list(projects.values()),openFile,indent=4)