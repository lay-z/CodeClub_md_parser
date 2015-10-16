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
    dictionary = {}
    # for i,step in enumerate(file.split('\n# ')):
        


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
        return {
            'number': info_matches.group(1).strip(),
            'step_name': info_matches.group(2).strip(),
            'description': info_matches.group(3).strip()
        }
    
    
def get_heading(intro_section):
    '''
    Returns title the description if it finds it 
        else returns nothing (perhaps should return false?)
    @return: String title of intro_section
    '''
    title_info = re.compile(r'title: (.*)')
    matches = title_info.search(intro_section)
    if matches is not None:
        return matches.group(1).strip()

def parse_project(intro_section):
    '''
    Gets the project_description, project_image, and project_title in a 
    dictionary. 
    @param intro_section: Data 
    @return dictionary of project_description, project_image and project_title
    '''

def split_step(step):
    '''
    Splits up a step into into its respective components (e.g. activity check list etc)
    The Description of the step is removed from the returned list
    @param step: Step of a CodeClub Project
    @return list of steps split up (excluding description)
    '''
    return step.split('\n## ')[1:]

def parse_step_section(step_section):
    '''
    Parses through step section and returns dictionary with header and data
    @param step_section: section within step
    @return dictionary containing step header and step data
    '''
    regex = re.compile(r'(.*)\{ \.\w{1}([]*)')
    matches = regex.search(step_section)
    if matches is not None:
        return {
            'header': matches.group(1),
            'body': matches.group(2),
        }

if __name__ == '__main__':
    #This code will when not being imported in another file
    # json.dump(dictionary, json_file)
    
    file = open("Flappy Parrot.md", "r").read()

    # test get_heading
    intro = open("flappy_parrot/step0.md", "r").read()

    print get_heading(intro)

    # test parse_step
    step_info = open("flappy_parrot/step7.md", "r").read()

    # print step_info
    print parse_step(step_info)

    # test split_step
    # for step in split_step(step_info):
    #     print parse_step_section(step)
    
    
    