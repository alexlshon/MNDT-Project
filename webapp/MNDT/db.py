import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

# returns a connect to the database for a flask app instance.
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    # Initializes the schema for the posts table
    with current_app.open_resource('./static/schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

    # Initializes the data in the csv and places it into the posts table in the sql sever
    with current_app.open_resource('./static/test_file.csv','r')  as f:
        d = [tuple(line.split(',')) for line in f.read().splitlines()]
        db.executemany('INSERT INTO test (\'tweet_text\',\'post_time\',\'origin_long\',\'origin_lat\',\'latitude\',\'longitude\',\'predicted_relevant\') VALUES (?,?,?,?,?,?,?)', d)


# This creates the command to initialize the data base from the bash shell
@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
