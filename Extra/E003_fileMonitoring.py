import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Handler(FileSystemEventHandler):
    def on_moved(self, event):
        print(event)
    def on_created(self, event):
        print(event)
    def on_deleted(self, event):
        print(event)
    def on_modified(self, event):
        print(event)

if __name__ == '__main__':
    watchDir1 = r".\\"
    observer = Observer()  # observer객체를 만듦
    event_handler1 = Handler()
    observer.schedule(event_handler1, watchDir1, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except:
        observer.stop()
        observer.join()
        print("Error")