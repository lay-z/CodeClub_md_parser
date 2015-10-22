import re

def parse_component(text):
    '''Parse component takes a block of text and returns an object consisting of
        text
        blocks
        image
    '''

    result = {}

    blockPattern = re.compile(r'```blocks([^`]*)```')

    # find blocks
    match = blockPattern.search(text)
    if (match is not None):
        result['blocks'] = match.group(1).strip()

    # remove blocks
    text = blockPattern.sub('',text)
    # print('text',text)

    imagePattern = re.compile(r'!\[screenshot\]\((.*)\)')

    # find images
    match = imagePattern.search(text)
    if (match is not None):
        result['image'] = match.group(1).strip()

    # remove images
    result['text']  = imagePattern.sub('',text).strip()

    return result