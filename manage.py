from flask_script import Manager

from flamorphy import create_app

app = create_app(__name__)
manager = Manager(app)


@manager.command
def runserver(host='0.0.0.0', port=None):
    """Starts a lightweight development Web server on the local machine."""
    default_port = app.config['PORT']
    if host == 'localhost':
        host = '127.0.0.1'
    port = port if port else default_port
    app.run(debug=True, host=host, port=int(port))


if __name__ == '__main__':
    manager.run()
