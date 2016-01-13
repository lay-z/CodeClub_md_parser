import object_formatter

class Language:

    def __init__(self,collection):
        """Initialise a language with a interface to communicate with 
        a mongodb language collection.

        @params
            collection - interface to communicate with mongo collection
        """

        self.language = {}
        self.collection = collection

    def load(self,language):
        """Load a language from a dictionary object into memory
        """

        self.language = language

    def update(self,language):
        """Update the internal representation of the language
        """

        for key, value in language.items():
            self.language[key] = value

    def format(self,url):
        """Format the language to ensure the image paths are correct
        """

        object_formatter.changeImagePath(self.language,url)

    def save(self):
        """Save the given language using the mongo collection interface
        """

        self.language = self.collection.update(
            { "name" : self.language['name'] },
            self.language
            )
