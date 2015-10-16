import json
import re

    
def split_sections(file_content):
    '''
    @params file_content: .md file being split up into sections expects it to already
                        have been opened
    @return dictionary: will return dictionary with section names as keys
                        values will be file objects of respective sections
    Splits a file into its respective sections
    '''
    dictionary = {}
    # for i,step in enumerate(file.split('\n# ')):
        


def parse_step(step):
    '''
    gets the step_title, the number, and the step_description (create a dictionary with it)
    @params step: string object of a step to parse step information from
    @return dictionary
    '''
# \n# .*
    step_info = re.compile(r'\*\*Step (\d+):\*\* ([^\{]*)')
    info_matches = step_info.search(step)
    description_info = re.compile(r'\}\n\n(.*)\n\n## ', re.DOTALL) # DOTALL used so that '.' also matches '\n'
    description_matches = description_info.search(step)

    if(info_matches is not None):
        return {
            'number': info_matches.group(1).strip(),
            'step_name': info_matches.group(2).strip(),
            'description': description_matches.group(1) if description_matches else None # Python equivilant to turnary expression
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


if __name__ == '__main__':
    #This code will when not being imported in another file
    # json.dump(dictionary, json_file)
    
    file = open("Flappy Parrot.md", "r").read()

    # test get_heading
    intro = open("flappy_parrot/step0.md", "r").read()

    print get_heading(intro)

    # test parse_step
    step_info = open("flappy_parrot/step3.md", "r").read()
    # print step_info

    print parse_step(step_info)
    
    
    