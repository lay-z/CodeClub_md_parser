class Project:

    def __init__(self,collection):
        """Initialise a project with a interface to communicate with 
        a mongodb project collection.

        @params
            collection - interface to communicate with mongo collection
        """

        pass

    def load(self,project):
        """Load a project from a dictionary object into memory
        """

        pass

    def update(self,project):
        """Update the internal representation of the project
        """

        pass

    def format(self):
        """Format the project to ensure the image paths are correct
        """

        pass

    def save(self):
        """Save the given project using the mongo collection interface
        """

        pass