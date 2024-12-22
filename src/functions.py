import eel
from utils import get_logger

logger = get_logger(__name__)


@eel.expose
def say_hello_py(x):
    logger.info(x)


@eel.expose
def get_current_page():
    # Calls JS function whatPage()
    eel.whatPage()
