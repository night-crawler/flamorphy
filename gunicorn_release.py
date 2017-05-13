bind = ['127.0.0.1:1681', 'unix:/venv/run/gunicorn.sock']
workers = 4
pid = '/venv/run/gunicorn.pid'
reload = True
preload_app = True
chdir = '/venv/application/'
pythonpath = '/venv/bin/python'
raw_env = [
    'LANG=ru_RU.UTF-8',
    'LC_ALL=ru_RU.UTF-8',
    'LC_LANG=ru_RU.UTF-8'
]
user = 'flamorphy'
group = 'flamorphy'
accesslog = '/venv/log/flamorphy.access.log'
errorlog = '/venv/log/flamorphy.error.log'
timeout = 10
