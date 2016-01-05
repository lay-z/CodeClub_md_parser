import re

def parse_notes(project_notes):
    """Given a text document containing the supporting notes for a
    CodeClub scratch project
    """

    result = {}

    scratch_link_search = Search(
        project_notes,
        r'\[jumpto\.cc/[^\]]*resources]\(([^:]*://jumpto.cc/[^\)]*)\)',
        1
    )

    if (scratch_link_search.check()):
        scratch_link = scratch_link_search.match()
        result.update({'link' : scratch_link})

    return result
    

class Search:

    def __init__(self,text,expresssion,group=0):
        self.text = text
        self.group = group
        self.pattern = re.compile(expresssion)

    def check(self):
        self.result = self.pattern.search(self.text)
        return (
            (self.result is not None) and
            (self.result.group(self.group) is not None)
            )

    def match(self):
        if (('match' not in dir(self)) and (not self.check(self.text))):
            raise RuntimeError('There is no matching text')
        return self.result.group(self.group)

# def regex_search_list(text,search_list,default=''):
# 	"""Given a certain text and a list of regular expressions 
# 	"""

#     for search in search_list:

#         Search(text,search_list.get('expression'),search_list.get('group'))
#         if (search.check()):
#             return search.match()

#     return default
