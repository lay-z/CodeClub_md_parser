import os
import re
import glob
import json
import urllib.parse

def buildRootUrl(url,filename):
    """Build a root url from the base url and a directory
    """

    if (filename.startswith('data:image') or filename.startswith('http')):
        return filename

    return url + urllib.parse.quote(filename)

def changeImagePath(dictionary,url):
    """Recusrively look into dictionary to chagne the image keys to prepend a root url
    """

    if (type(dictionary) is not dict):
        return

    for key in dictionary:
        if ((key in ['image','display']) and (dictionary[key] is not None)):
            dictionary[key] = buildRootUrl(url,dictionary[key])
        elif (type(dictionary[key]) == dict):
            changeImagePath(dictionary[key],url)
        elif (type(dictionary[key]) == list):
            for item in dictionary[key]:
                changeImagePath(item,url)


def addCheckmark(project):
    """Add a checkmark to all project components
    """

    for step in project.get('steps',[]):
        for component in step.get('components',[]):
            component['checkmark'] = True