# services/user/manage.py

from flask.cli import FlaskGroup

from project import app, db #new

cli = FlaskGroup(app)

# new
#This register a new command recreate_db, to the cli
#so that we can run it from CLI, which we'll use shortlly to apply the model to the database
@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    cli()
