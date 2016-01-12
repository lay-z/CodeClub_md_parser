import os
import re
import json
import collections

import config
import database_writer

def main():

    environment = os.environ.get('PYTHON_ENV','development')
    pythonMongolabUri = config.pythonMongolabUri[environment]
    collection = database_writer.DatabaseWriter(
                                                'challenges',
                                                pythonMongolabUri
                                                )

    for challenge in collection.query():

        components = []
        if (challenge['script']['format'] == 'markdown'):
            components = parseScript(challenge['script']['content'])

        project = collections.OrderedDict([
            ('name', re.sub(r'\W+','_',challenge['name'].lower())),
            ('title', challenge['name']),
            ('description', challenge['summary']),
            ('steps', [
                collections.OrderedDict([
                    ('name', 'Imported Steps'),
                    ('description', 'These steps have been imported from Python Challenges'),
                    ('components', components)
                ])
            ])
        ])

        # If needed create a folder
        os.makedirs('projects/python/{name}'.format(**project), exist_ok=True)

        # Save the project definition
        filename = 'projects/python/{name}/{name}.json'.format(**project)
        json.dump(project,open(filename,'w'),indent=4)

        # Save the template file
        filename = 'projects/python/{name}/{name}.py'.format(**project)
        open(filename,'w').write(challenge['code'])

def parseScript(script):
    """Split script into components"""

    components = []
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