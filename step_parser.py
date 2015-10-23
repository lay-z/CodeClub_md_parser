import re
import json

from component_parser import parse_component

def parse_step(raw_step):
    '''
    gets the step_title, the number, and the step_description (create a dictionary with it)
    @params step: string object of a step to parse step information from
    @return dictionary
    '''

    step_info = re.compile(r'\**Step (\d+):\** ([^\{]*)\{*.*\}*([^#]*)')
    info_matches = step_info.search(raw_step)

    if(info_matches is not None):

        # Populate key step information
        step = {
            'number': info_matches.group(1).strip(),
            'title': info_matches.group(2).strip(),
            'description': info_matches.group(3).strip()
        }

        # Extract step and challenges
        raw_step, raw_challenges = split_steps(raw_step)

        print(raw_step,'\n' + ('='*80) + '\n',raw_challenges[:1])

        # Format step section
        step_section = parse_step_sections(raw_step)
        formated_step = split_step_section(step_section)
        step.update(formated_step)

        # Format all challenge sections
        challenges = []
        for raw_challenge in raw_challenges:
            challenge = parse_challenge(raw_challenge)
            challenges.append(challenge)

        return step, challenges

def parse_challenge(raw_challenge):
    '''
    gets the title, the number, and the description (create a dictionary with it)
    @params step: string object of a step to parse step information from
    @return dictionary
    '''

    challenge_info = re.compile(r'(\d*):\** ([^\{]*)\{*[^\}]*\}*\s*(.*)\+*')
    info_matches = challenge_info.search(raw_challenge)
    raw_challenge = challenge_info.sub('',raw_challenge)

    if(info_matches is not None):

        # Populate key step information
        challenge = {
            'number': info_matches.group(1).strip(),
            'title': info_matches.group(2).strip(),
            'description': info_matches.group(3).strip(),
            'challenge' : True
        }

        raw_challenge_sections = [item.strip() for item in raw_challenge.split('\n## ') if (len(item.strip()) > 0)]

        if (len(raw_challenge_sections) is 0):
            return challenge

        formated_challenge = split_step_section({'components':raw_challenge_sections[0]})
        challenge.update(formated_challenge)

        for raw_challenge_section in raw_challenge_sections[1:]:
            challenge_section = parse_step_sections(raw_challenge_section)
            formated_challenge = split_step_section(challenge_section)
            challenge.update(formated_challenge)

        return challenge

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
    # print split_challenges
    step = split_challenges[0].split('\n## ')[1:]
    # challenges = [split_challenge.split('\n## ') for split_challenge in split_challenges[1:]]
    challenges = split_challenges[1:]

    return step, challenges

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
    
def split_step_section(section):
    for key, value in section.items():
        section[key] = []
        component = value.split('\n+ ')
        for part in component:
            section[key].append(parse_component(part))
    return section

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
