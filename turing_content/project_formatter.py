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