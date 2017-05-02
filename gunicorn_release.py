# release config for gunicorn
# TODO: fill it out!

bind = '127.0.0.1:1681'
workers = 1
# pid = ''
reload = True
preload_app = True
# chdir = ''
# pythonpath = ''
raw_env = [
    'LANG=ru_RU.UTF-8',
    'LC_ALL=ru_RU.UTF-8',
    'LC_LANG=ru_RU.UTF-8'
]
# user = ''
# group = ''
# accesslog = ''
# errorlog = ''
timeout = 10
