import environ

from os import path

env = environ.Env(DEBUG=(bool, False),) # set default values and casting

ROOT_DIR = environ.Path(__file__) - 2
APP_DIR = ROOT_DIR.path('bot')

READ_DOT_ENV_FILE = env.bool('APP_READ_DOT_ENV_FILE', default=False)
if READ_DOT_ENV_FILE:
	# OS environment variables take precedence over variables from .env
	env.read_env(str(ROOT_DIR.path('.env')))

CONFIG_DIR = env.path('CONFIG_DIR', default=ROOT_DIR.path('config'))

LOGGING_CONFIG_FILE = CONFIG_DIR('logging.ini')