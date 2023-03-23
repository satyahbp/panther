from datetime import datetime

from panther import version
from panther.utils import generate_secret_key

apis_py = """from datetime import datetime

from panther.app import API
from panther.configs import config
from panther import version, status
from panther.request import Request
from panther.response import Response
from app.throttling import InfoThrottling


@API()
async def hello_world_api():
    return {'detail': 'Hello World'}


@API(cache=True, throttling=InfoThrottling)
async def info_api(request: Request):
    data = {
        'version': version(),
        'datetime_now': datetime.now().isoformat(),
        'user_agent': request.headers.user_agent,
        'db_engine': config['db_engine'],
    }
    return Response(data=data, status_code=status.HTTP_202_ACCEPTED)
"""

models_py = """from panther.db import Model
"""

serializers_py = """from pydantic import BaseModel as Serializer
"""

throttling_py = """from datetime import timedelta
from panther.throttling import Throttling


InfoThrottling = Throttling(rate=5, duration=timedelta(minutes=1))
"""

app_urls_py = """from app.apis import hello_world_api, info_api

urls = {
    '': hello_world_api,
    'info/': info_api,
}
"""

configs_py = """\"""
{PROJECT_NAME} Project (Generated by Panther on %s)
\"""

from pathlib import Path
from panther.utils import load_env


BASE_DIR = Path(__name__).resolve().parent
env = load_env(BASE_DIR / '.env')

DB_NAME = env['DB_NAME']
SECRET_KEY = env['SECRET_KEY']


MIDDLEWARES = [
    ('panther.middlewares.db.Middleware', {'url': f'pantherdb://{BASE_DIR}/{DB_NAME}.pantherdb'}),
]

USER_MODEL = 'panther.db.models.User'

MONITORING = True

LOG_QUERIES = True

URLs = 'core/urls.py'
""" % datetime.now().date().isoformat()

middlewares = """from panther.middlewares import BaseMiddleware
"""

env = """
SECRET_KEY = '%s'

DB_NAME = '{PROJECT_NAME}'
""" % generate_secret_key()

main_py = """from panther import Panther

app = Panther(__name__)
"""

urls_py = """from app.urls import urls as app_urls

urls = {
    '/': app_urls, 
}
"""

git_ignore = """__pycache__/
.venv/
.idea/
.env
logs/
*.pantherdb
"""

requirements = """panther==%s
""" % version()

Template = {
    'app': {
        'apis.py': apis_py,
        'models.py': models_py,
        'serializers.py': serializers_py,
        'urls.py': app_urls_py,
    },
    'core': {
        'configs.py': configs_py,
        'middlewares.py': middlewares,
        'urls.py': urls_py,
    },
    'main.py': main_py,
    '.env': env,
    '.gitignore': git_ignore,
    'requirements.txt': requirements,
}
