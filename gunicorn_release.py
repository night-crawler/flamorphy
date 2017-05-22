import os

bind = ['0.0.0.0:1681', 'unix:/application/run/gunicorn.sock']
workers = os.environ.get('GUNICORN_WORKERS', 4)
pid = '/application/run/gunicorn.pid'
reload = True
preload_app = True
chdir = '/application/flamorphy/'
pythonpath = '/usr/local/bin/python'
raw_env = [
    'LANG=ru_RU.UTF-8',
    'LC_ALL=ru_RU.UTF-8',
    'LC_LANG=ru_RU.UTF-8'
]
user = 'flamorphy'
group = 'flamorphy'
accesslog = '/application/log/gunicorn.access.log'
errorlog = '/application/log/gunicorn.error.log'
timeout = os.environ.get('GUNICORN_TIMEOUT', 10)
