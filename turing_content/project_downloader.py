import os
import re
import json
import collections

import config
import database_writer

def main():

    environment = os.environ.get('PYTHON_ENV','development')
    pythonMongolabUri = config.pythonMongolabUri[environment]
    users = database_writer.DatabaseWriter('users',pythonMongolabUri)
    challenges = database_writer.DatabaseWriter('challenges',pythonMongolabUri)
    environments = database_writer.DatabaseWriter('environments',pythonMongolabUri)

    # Download all the users
    for user in users.query():
        os.makedirs('downloaded/users', exist_ok=True)
        filename = 'downloaded/users/{_id}.json'.format(**user)
        user = collections.OrderedDict(
            [(key, user[key]) for key in ['name','email']]
            )
        json.dump(user,open(filename,'w'),indent=4)        

    # Download all the challenges
    for challenge in challenges.query():

        components = []
        if (challenge['script']['format'] == 'markdown'):
            components = parseScript(challenge['script']['content'])

        project = collections.OrderedDict([
            ('id', str(challenge['_id'])),
            ('name', re.sub(r'\W+','_',challenge['name'].strip().lower())),
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
        os.makedirs('downloaded/projects/{name}'.format(**project), exist_ok=True)

        # Save the project definition
        filename = 'downloaded/projects/{name}/{name}.json'.format(**project)
        json.dump(project,open(filename,'w'),indent=4)

        # Save the template file
        filename = 'downloaded/projects/{name}/{name}.py'.format(**project)
        open(filename,'w').write(challenge['code'])

        # Remove this line to download environments for users
        continue

        # Download all environments
        for environment in environments.query({'challenge':challenge['_id']}):

            data = {
                'project': project['name'],
                'user': environment['user']
            }

            os.makedirs('downloaded/projects/{project}/environments'.format(**data), exist_ok=True)
            filename = 'downloaded/projects/{project}/environments/{user}.py'.format(**data)
            open(filename,'w').write(environment['code'])


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
        component['code'] = {
            'language': 'python',
            'content': match.group(1).strip()
            }

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