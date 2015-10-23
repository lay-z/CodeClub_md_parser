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


if (__name__ == "__main__"):
    text = '''Delete the code that uses the mouse to control the boat:\n\n```blocks\n    if < (distance to [mouse-pointer v]) > [5] > then\n        point towards [mouse-pointer v]\n        move (1) steps\n    end\n```\n\n...and replace it with code to control the boat using the arrow keys.\n\nThis is the code you'll need to move the boat forward:\n\n```blocks\n    if < key [up arrow v] pressed? > then\n        move (1) steps\n    end\n```\n\nYou'll also need code to `turn` {.blockmotion} the boat when the left and right arrow keys are pressed.'''
    print(parse_component(text))