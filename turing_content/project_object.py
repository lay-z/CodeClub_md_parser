import project_formatter

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

        project_formatter.changeImagePath(self.project,url)

    def save(self):
        """Save the given project using the mongo collection interface
        """

        self.project = self.collection.update(
            { "title" : self.project['title'] },
            self.project
            )
