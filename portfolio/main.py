from flask import Blueprint, render_template
from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    current_year = datetime.now().year
    return render_template('index.html', year=current_year)