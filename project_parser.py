import json
import re

from step_parser import parse_step
    
def split_project(file_content):
    '''
    Splits a CodeClub project into respective steps
    @params file_content: .md file being split up into sections expects it to already
                        have been opened and read
    @return dictionary: will return dictionary with section names as keys
                        values will be file objects of respective sections
    '''
    sections = file_content.split('\n# ')
    steps = sections[2:] # Because first 2 sections are intro and project_info
    project = {
        'title': get_title(sections[0])
    } 
    project.update(parse_intro(sections[1]))
    project['steps'] = []

    for step in steps:
        step_obj = parse_step(step)
        project['steps'].append(step_obj)

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
    intro_text = re.compile(r'\}\n\n(.*)', re.DOTALL).search(intro_section).group(1)
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


    
    
    