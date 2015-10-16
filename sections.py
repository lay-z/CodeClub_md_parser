import json
import re

    
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
        'project_title': get_title(sections[0])
    } 
    project.update(parse_intro(sections[1]))
    project['steps'] = []

    for step in steps:
        step_obj = parse_step(step)
        project['steps'].append(parse_step(step))
        project

    print project


def parse_step(step):
    '''
    gets the step_title, the number, and the step_description (create a dictionary with it)
    @params step: string object of a step to parse step information from
    @return dictionary
    '''

    step_info = re.compile(r'\*\*Step (\d+):\*\* ([^\{]*)\{*.*\}*([^#]*)')
    info_matches = step_info.search(step)
    # # description_info = re.compile(r'\}\n\n(.*)\n\n## ', re.DOTALL) # DOTALL used so that '.' also matches '\n'
    # description_info = re.compile(r'([^#]*)')
    # description_matches = description_info.search(step)

    if(info_matches is not None):
        result = {
            'number': info_matches.group(1).strip(),
            'title': info_matches.group(2).strip(),
            'description': info_matches.group(3).strip()
        }
        formated_step = parse_step_sections(split_steps(step))
        result.update(formated_step)
        return result
    
    
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

    return {
        'project_image': photo.group(1).strip() if photo else None,
        'project_description': description.strip() if description else None 
    }

def split_steps(step):
    '''
    Splits up a step into into its respective components (e.g. activity check list etc)
    The Description of the step is removed from the returned list
    First removes the challenges and then splits into steps
    @param step: Step of a CodeClub Project
    @return dictionary of step_sections. Keys to dictionary are the section headers,
            values are step_section data (to be parsed later :P)
    '''

    #Split up by challenges
    split_challenges = step.split('\n## Challenge')
    print split_challenges

    print split_challenges[0].split('\n## ')[1:]

def parse_step_sections(step_sections):
    '''
    Parses through each of the step sections and returns dictionary with header and data
    @param step_section (list): List of step_sections in step
    @return dictionary containing step header and step data
    '''
    header_search = re.compile(r'(.*)\{.*\}\n\n')
    result = {}

    for section in step_sections:
        matches = header_search.search(section)

        if matches is not None:
            # Get the data related to the result
            key = find_key(matches.group(1).strip()) 
            if key is not None:
                result[key] = header_search.sub('', section).strip()

    return result

def find_key(heading):
    '''
    Returns respective key to the heading
    @param heading (String): Heading of the step
    @return (String): String as key
    '''
    try: 
        return {
            'Activity Checklist': 'components',
            'Test Your Project': 'tests',
            'Things to try': 'extensions',
        }[heading]
    except KeyError:
        return None
    

if __name__ == '__main__':
    #This code will when not being imported in another file
    # json.dump(dictionary, json_file)
    
    project = open("Flappy Parrot.md", "r").read()

    # test get_title
    intro = open("flappy_parrot/step0.md", "r").read()

    # print get_title(intro)

    # test parse_step
    step_info = open("flappy_parrot/step8.md", "r").read()
    split_steps(step_info)

    # print step_info
    # print parse_step(step_info)

    # test split_step
    # print parse_step(step_info)


    
    
    