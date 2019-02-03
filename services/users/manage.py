# services/users/manage.py

from flask.cli import FlaskGroup

from project import app


cli = FlaskGroup(app) #created a new FlaskGroup instance to extend the normal CLI with command related to the Flask App

if __name__ == '__main__':
    cli()
