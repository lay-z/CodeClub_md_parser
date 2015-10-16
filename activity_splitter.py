import json

def split_activities(section):
    test2 = section.split('\n+ ')
    for part in test2:
        
    

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