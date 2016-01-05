import os
import re
import glob
import json
import urllib.parse

import config

def build_root_url(url,filename):
    """Build a root url from the base url and a directory
    """

    if (filename.startswith('data:image') or filename.startswith('http://')):
        return filename

    return url + urllib.parse.quote(filename)

def change_image_path(dictionary,url):
    """Recusrively look into dictionary to chagne the image keys to prepend a root url
    """

    if (type(dictionary) is not dict):
        return

    for key in dictionary:
        if ((key == 'image') and (dictionary[key] is not None)):
            dictionary[key] = build_root_url(url,dictionary[key])
        elif (type(dictionary[key]) == dict):
            change_image_path(dictionary[key],url)
        elif (type(dictionary[key]) == list):
            for item in dictionary[key]:
                change_image_path(item,url)


def find_projects():
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
        change_image_path(project,config.imageRoot)

        # Add to list of projects
        projects.append(project)

    return projects

if (__name__ == "__main__"):

    projects = find_projects()

    with open('data/projects_output.json','w') as openFile:
        json.dump(projects,openFile,indent=4)