import os

from flask_script import Manager, Server
from setuptools import find_packages

from thor.app import create_app
from thor.exts import db


app_root = os.path.dirname(os.path.realpath(__name__))

application = create_app('Thor')
server = Server(host='0.0.0.0', port=5000)
manager = Manager(application)
manager.add_command("runserver", server)


def _import_models():
    packages = find_packages('./thor/modules')
    for each in packages:
        guess_module_name = 'thor.modules.%s.models' % each
        try:
            __import__(guess_module_name, globals(), locals())
            print('Find model:', guess_module_name)
        except ImportError:
            pass


@manager.command
def syncdb():
    with application.test_request_context():
        _import_models()
        db.create_all()
        db.session.commit()
    print('Database Created')


@manager.command
def dropdb():
    with application.test_request_context():
        db.drop_all()
    print('Database Dropped')


if __name__ == '__main__':
    manager.run()
