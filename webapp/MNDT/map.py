from flask import (
    Blueprint, g, render_template,current_app
)
from MNDT.db import get_db
import csv

bp = Blueprint('map', __name__)

@bp.route('/')
def map():
    db = get_db()

    posts = db.execute(
    '''
    SELECT  tweet_text, latitude, longitude
    FROM test
    WHERE predicted_relevant = 1
    '''
    ).fetchall()
    return render_template('map/index.html',data = posts)
