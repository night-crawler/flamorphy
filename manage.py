#!/usr/bin/env python
from flask_script import Manager

from app import app
from app.config import configure_app, BaseConfig


manager = Manager(app)


@manager.command
def runserver():
    configure_app(app, config_name='dev')

    app.run(host='127.0.0.1', port=BaseConfig.PORT)


if __name__ == '__main__':
    manager.run()
