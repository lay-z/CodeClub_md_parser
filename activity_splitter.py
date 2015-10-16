# import json
# import re
#
#
# #split to {Ativy chck: some stuf ...}
#
# def split_activities(section):
#     test2 = section.split('\n+ ')
#     for part in test2:
#
#
# pattern = re.compile(r```blocks[^`]*```,test2)
# re.match(r```blocks[^`]*```,test2)
#
# testfile = open("act-test.md", "r").read()
# split_activities(testfile)







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
import json

# DEBUG = False

def splitSubsection(section):
    for key, value in section.items():
        #result = []
        section[key] = []
        if(key == "tests"):
            section[key] = [parseComponent(value)]
        else:
            component = value.split('\n+ ')
            for part in component:
                # splitComponent = parseComponent(part)
                #result.append(parseComponent(part))
                section[key].append(parseComponent(part))
            #section[key] = result
    return section

# def splitSubsection2(section):
#     for key, value in section.items():
#         section[key] = []
#         component = value.split('\n+ ')
#         for part in component:
#             print("----------")
#             print(component)
#             # splitComponent = parseComponent(part)
#             #result.append(parseComponent(part))
#             section[key].append(parseComponent(part))
#         #section[key] = result
#     return section

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
		# if DEBUG: print('blocks:',result['blocks'])

	# remove blocks
	text = blockPattern.sub('',text)
	# print('text',text)

	photoPattern = re.compile(r'!\[screenshot\]\((.*)\)')

	# find photos
	match = photoPattern.search(text)
	if (match is not None):
		result['photo'] = match.group(1).strip()
		# if DEBUG: print('photo:',result['photo'] )

	# remove photos
	result['text']  = photoPattern.sub('',text).strip()
	# if DEBUG: print('text:',result['text'])

	return result


if (__name__ == "__main__"):


    test = {"tests":"fsfdsfdsfwfwfw",
            "checklist":"""
            + Let's add a sound to play when Flappy scores a point. Click on the **Pipe** sprite add a score sound. **bird** is a good choice.
            + Now click back on the `Scripts` {.blockgrey} tab.
            + Make a new variable `For all sprites` {.blockgrey} and call it `score` {.blockorange}.
            + Add a block to set the score to 0 when the flag is clicked.
            + Add the following block:
            ```blocks
                when I start as a clone
                    wait until <(x position) < ([x position v] of [Flappy v])>
                    change [score v] by (1)
                    play sound [bird v]
            ```"""

            }


    # """
    # + Let's add a sound to play when Flappy scores a point. Click on the **Pipe** sprite add a score sound. **bird** is a good choice.
    # + Now click back on the `Scripts` {.blockgrey} tab.
    # + Make a new variable `For all sprites` {.blockgrey} and call it `score` {.blockorange}.
    # + Add a block to set the score to 0 when the flag is clicked.
    # + Add the following block:
    # ```blocks
    #     when I start as a clone
    #         wait until <(x position) < ([x position v] of [Flappy v])>
    #         change [score v] by (1)
    #         play sound [bird v]
    # ```
    #         """
    split_up = splitSubsection2(test)
    #print (split_up["checklist"][0]["text"])
    # print(split_up[0]["blocks"])
    # test =

    # split_up = splitSubsection(test)
    # print split_up[0]

	# DEBUG = True
	# parseComponent(test)
