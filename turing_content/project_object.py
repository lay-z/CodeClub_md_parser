import object_formatter

class Project:

    def __init__(self,collection):
        """Initialise a project with a interface to communicate with 
        a mongodb project collection.

        @params
            collection - interface to communicate with mongo collection
        """

        self.project = {}
        self.collection = collection

    def load(self,project):
        """Load a project from a dictionary object into memory
        """

        self.project = project

    def update(self,project):
        """Update the internal representation of the project
        """

        for key, value in project.items():
            self.project[key] = value

    def format(self,url):
        """Format the project to ensure the image paths are correct
        """

        object_formatter.changeImagePath(self.project,url)

        if (self.project.get('language','') == 'Scratch'):
            object_formatter.addCheckmark(self.project)

    def save(self,environment="development"):
        """Save the given project using the mongo collection interface
        """

        if (self.project.get('draft',False) and (environment == "production")):
            return

        self.project = self.collection.update(
            { "title" : self.project['title'] },
            self.project
            )
