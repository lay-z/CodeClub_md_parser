import json
import re

from step_parser import parse_step
    
def parse_project(file_content):
    '''
    Splits a CodeClub project into respective steps
    @params file_content: .md file being split up into sections expects it to already
                        have been opened and read
    @return dictionary: will return dictionary with section names as keys
                        values will be file objects of respective sections
    '''
    sections = re.split(r'\n#[^#]',file_content)
    steps = sections[2:] # Because first 2 sections are intro and project_info
    project = {
        'title': get_title(sections[0])
    } 
    project.update(parse_intro(sections[1]))
    project['steps'] = []

    for raw_step in steps:
        step, challenges = parse_step(raw_step)
        project['steps'].append(step)

        # Add all challenges
        for challenge in challenges:
            project['steps'].append(challenge)

    return project

    
def get_title(project_info):
    '''
    Returns title the description if it finds it 
        else returns nothing (perhaps should return false?)
    @return: String title of project_info
    '''
    title_info = re.compile(r'title: (.*)')
    matches = title_info.search(project_info)
    if matches is not None:
        return matches.group(1).strip()

def parse_intro(intro_section):
    '''
    Gets the project_description and project_image from the intro section
    dictionary. 
    @param intro_section: Data 
    @return dictionary of project_description, project_image 
    '''
    photoPattern = re.compile(r'!\[screenshot\]\((.*)\)')
    intro_match = re.search(r'\}\n([^#]*)',intro_section)

    if (intro_match is not None):
        intro_text = intro_match.group(1)
    else:
        intro_text = intro_section

    photo = photoPattern.search(intro_section)
    description = photoPattern.sub('', intro_text)

    if (photo is None):
        photoPattern = re.compile(r'''<img src="(.*)">''')
        photo = photoPattern.search(intro_text)
        description = photoPattern.sub('', intro_text)


    return {
        'image': photo.group(1).strip() if photo else None,
        'description': description.strip() if description else None 
    }


if __name__ == '__main__':
    #This code will when not being imported in another file
    # json.dump(dictionary, json_file)
    
    project = open("Flappy Parrot.md", "r").read()
    output = open("flappy parrot.json", "w")
    json.dump(split_project(project), output, indent = 4)

    # test get_title
    # intro = open("flappy_parrot/step0.md", "r").read()

    # print get_title(intro)

    # test parse_step
    # step_info = open("flappy_parrot/step8.md", "r").read()
    # split_steps(step_info)

    # print step_info
    # print parse_step(step_info)

    # test split_step
    # print parse_step(step_info)


    
    
    