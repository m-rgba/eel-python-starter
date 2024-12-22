# eel-python-starter

Starter for Python-Eel, PyWebview, and PyInstaller (w/ a Docker dev environment).

*w/ some optional AlpineJS sprinkled on top.*

## Structure
- Everything on the outer layer is orchestration for creating the dev environment, dependancies, and PyInstaller builders.
- `src` contains the application's files.
    - The `.py` files in `src` contain the routes and background processes.
    - Functions decorated with `@eel.expose` are available in JS.
    - `src/web` are all the Jinja templates and frontend assets which will be served.
        - `src/web/templates/layout.html` contains the layout that the other templates inherit from.
        - JS defined with `eel.expose(function_name);` are available in Python.

## How to run development Docker container

```
docker compose up
```

It'll then be running at `http://localhost:8000`

## How to create binary

1. Install Python and virtualenv

Homebrew (Mac):
```
brew install virtualenv
```

In directory:
```
virtualenv -p python3 venv_name 
```

Activate:
```
source venv_name/bin/activate
```

2. Install requirements to venv

```
pip install -r requirements.txt
```

3. Create distributable binary

```
pyinstaller Eel.spec
```

File will be available in `/dist`