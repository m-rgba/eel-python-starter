from bottle import Bottle, template
import jinja2
import os
from utils import get_base_path, get_logger

logger = get_logger(__name__)

# Get web path
web_path = os.path.join(get_base_path(), "web")

# Setup Jinja2 environment
template_loader = jinja2.FileSystemLoader(os.path.join(web_path, "templates"))
template_env = jinja2.Environment(loader=template_loader)

# Create a Bottle app to handle custom routes
app = Bottle()


def render_template(template_name, kwargs=None):
    if kwargs is None:
        kwargs = {}
    template = template_env.get_template(template_name)
    return template.render(**kwargs)


@app.error(404)
def error404(error):
    return "Nothing here, sorry"


@app.route("/hello")
def hello():
    return render_template("hello.html")


@app.route("/world")
def world():
    return render_template("world.html")
