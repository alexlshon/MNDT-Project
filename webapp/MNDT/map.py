from flask import (
    Blueprint, g, render_template
)
from MNDT.db import get_db
import csv

bp = Blueprint('map', __name__)

def get_data(fpath='./MNDT/static/test_file.csv'):
    file = open(fpath, 'r')
    return list(csv.DictReader(file))

@bp.route('/')
def map():
    return render_template('map/index.html',data = get_data())
