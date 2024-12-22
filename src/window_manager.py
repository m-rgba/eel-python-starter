import webview
import eel
from utils import is_running_in_docker, get_logger

logger = get_logger(__name__)


@eel.expose
def close_window():
    if not is_running_in_docker():
        webview.windows[0].destroy()
    else:
        logger.warning("[Docker] Close window action")


@eel.expose
def minimize_window():
    if not is_running_in_docker():
        webview.windows[0].minimize()
    else:
        logger.warning("[Docker] Minimize window action")


@eel.expose
def fullscreen_window():
    if not is_running_in_docker():
        webview.windows[0].toggle_fullscreen()
    else:
        logger.warning("[Docker] Fullscreen window action")


@eel.expose
def maximize_window():
    if not is_running_in_docker():
        webview.windows[0].maximize()
    else:
        logger.warning("[Docker] Maximize window action")


@eel.expose
def restore_window(width, height):
    if not is_running_in_docker():
        window = webview.windows[0]
        window.resize(800, 600)
        # Calculate center position
        x = (width - 800) // 2
        y = (height - 600) // 2
        window.move(x, y)
    else:
        logger.warning("[Docker] Restore window action")
