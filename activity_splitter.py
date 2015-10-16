import json
import re

def split_activities(section):
    test2 = section.split('\n+ ')
    for part in test2:
        

pattern = re.compile(r```blocks[^`]*```,test2)
re.match(r```blocks[^`]*```,test2)

testfile = open("act-test.md", "r").read()
split_activities(testfile)






    
# def split_sections(file):
#     '''
#     @params file: .md file being split up into sections
#     @return diction
#     '''

# for i,step in enumerate(file.split('\n# ')):
#     print('--------')
#     print(step[:100])
    
#     open('flappy_parrot/step{}.md'.format(i),'w').write(step)


# # json.dump(dictionary, json_file)
# print dictionary


# if __name__ == '__main__':
#     #This code will when not being imported in another file
#     dictionary = {'test': 2}
    
#     file = open("Flappy Parrot.md", "r").read()
#     json_file = open("test.json", 'w')
#```blocks[^`]*```

import re

DEBUG = False

def parseComponent(text):
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
		if DEBUG: print('blocks:',result['blocks'])

	# remove blocks
	text = blockPattern.sub('',text)
	# print('text',text)

	photoPattern = re.compile(r'!\[screenshot\]\((.*)\)')

	# find photos
	match = photoPattern.search(text)
	if (match is not None):
		result['photo'] = match.group(1).strip()
		if DEBUG: print('photo:',result['photo'] )

	# remove photos
	result['text']  = photoPattern.sub('',text).strip()
	if DEBUG: print('text:',result['text'])

	return result


if (__name__ == "__main__"):

	test = """
Give Flappy the following script:
```blocks
    when FLAG clicked
        go to x: (-50) y: (0)
        forever
            change y by (-3)
```
![screenshot](pipe_design.png)
	"""

	DEBUG = True
	parseComponent(test)