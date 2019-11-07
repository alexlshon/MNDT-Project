"""
This is the initialization file for the mapping natural disasters tweets project webapp. The foundation for this web app is based off the tutorial on the main flask website.
"""

import os
from flask import Flask

#Tis allows the use of multiple apps running on one sever for larger projects
def create_app(test_config=None):
    #Flask app constructor
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'MNDT.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Import the modler code
    from . import modeler as m
    model = m.modeler(app)
    model.RFC()

    # Import the database code
    from . import db
    db.init_app(app)

    # Import the map blueprint and code
    from . import map
    app.register_blueprint(map.bp)
    app.add_url_rule('/', endpoint = 'map')

    return app
