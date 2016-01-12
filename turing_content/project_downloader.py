import os
import re
import json

import config
import database_writer

def main():

    environment = os.environ.get('PYTHON_ENV','development')
    pythonMongolabUri = config.pythonMongolabUri[environment]
    collection = database_writer.DatabaseWriter(
                                                'challenges',
                                                pythonMongolabUri
                                                )

    challenges = collection.query()

    for challenge in challenges[:2]:

        project = {}
        project['name'] = challenge['name']
        project['description'] = challenge['summary']

        components = []
        if (challenge['script']['format'] == 'markdown'):
            components = parseScript(challenge['script']['content'])

        project['steps'] = [
            {
                'name': 'Imported Steps',
                'description': 'These steps have been imported from Python Challenges',
                'components': components
            }
        ]

        print(json.dumps(project,indent=4))

def parseScript(script):
    """Split script into components"""

    components = []
    print(script)
    matches = re.findall(r'#+([^#]*)', script)

    for match in matches:
        component = parseComponent(match)
        components.append(component)

    return components

def parseComponent(text):
    '''Parse component takes a block of text and returns an object with
    text, code and image'''

    component = {}

    codePattern = re.compile(r'```([^`]*)```')
    match = codePattern.search(text)
    if (match is not None):
        component['code'] = match.group(1).strip()

    text = codePattern.sub('',text)

    imagePattern = re.compile(r"""<img src=['"](.+)['"]>""")
    match = imagePattern.search(text)
    if (match is not None):
        print(match.group(0))
        component['image'] = match.group(1).strip()

    text  = imagePattern.sub('',text)

    linkPattern = re.compile(r"\[[^\]]+\]\(([^\)]+)\)")
    match = linkPattern.search(text)
    if (match is not None):
        component['link'] = match.group(1).strip()

    component['text']  = linkPattern.sub('',text).strip()

    return component

if (__name__ == "__main__"):
    main()