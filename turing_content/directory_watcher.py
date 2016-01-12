import sys
import time
import logging
import watchdog.observers
import watchdog.events

class UpdateEventHandler(watchdog.events.FileSystemEventHandler):
    """Event Handler to call a function on file system update"""

    def __init__(self, function):
        super(UpdateEventHandler, self).__init__()
        self.function = function

    def on_any_event(self,event):
        """When any change in filesystem is observed print event and
        call function"""

        print(event)
        self.function()

def updating():
    print('Updating')
        
def blocking():
    while True:
        time.sleep(1)

def eventLoop(
              updatingFunction=updating,
              blockingFunction=blocking,
              watchPath='.'
              ):

    eventHandler = UpdateEventHandler(updatingFunction)
    observer = watchdog.observers.Observer()
    observer.schedule(eventHandler, watchPath, recursive=True)
    observer.start()
    try:
        blockingFunction()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if (__name__ == "__main__"):
    eventLoop()