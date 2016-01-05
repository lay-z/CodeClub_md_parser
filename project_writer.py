import re
import json


def main():
    """
    Project writer creates a seperate json file for all projects
    """

    projects = json.load(open('data/projects.json'))

    for project in projects:

        project['name'] = re.sub(r'\W','_',project['title'].lower())
        project['show'] = False

        filename = 'projects/{number:02.0f}_{name}.json'.format(**project)
        json.dump(project,open(filename,'w'),indent=4,sort_keys=True)


if (__name__ == "__main__"):
    main()