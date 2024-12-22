import os
import eel
import threading
import time
import webview
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from routes import app
from utils import is_running_in_docker, get_base_path, get_logger

# Eel decorators
import functions
import window_manager

logger = get_logger(__name__)

# Initialize eel with the correct path
web_path = os.path.join(get_base_path(), "web")
eel.init(web_path, allowed_extensions=[".js", ".html", ".txt", ".htm", ".xhtml"])


class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".py") or event.src_path.endswith(".html"):
            logger.info(f"Detected change in {event.src_path}, restarting server...")
            os._exit(3)  # Exit with status 3 to trigger container restart


def start_app():
    if is_running_in_docker():
        # Setup file watcher in Docker
        event_handler = FileChangeHandler()
        observer = Observer()
        observer.schedule(event_handler, path=get_base_path(), recursive=True)
        observer.start()
        try:
            eel.start(
                "index.html",
                port=8000,
                host="0.0.0.0",
                size=(800, 600),
                shutdown_delay=0.5,
                app=app,
                mode=None,
                block=True,
            )
        finally:
            observer.stop()
            observer.join()
    else:
        # Start Eel in a separate thread for desktop mode
        eel_thread = threading.Thread(
            target=lambda: eel.start(
                "index.html",
                port=8000,
                host="0.0.0.0",
                size=(800, 600),
                shutdown_delay=0.5,
                app=app,
                mode=None,
                block=True,
            )
        )
        eel_thread.daemon = True
        eel_thread.start()

        # Give the Eel server time to start
        time.sleep(1)

        # Create and start webview in the main thread
        webview.create_window("Eel Webview", "http://localhost:8000", frameless=True)
        webview.start()


if __name__ == "__main__":
    start_app()
