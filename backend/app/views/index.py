from flask import Blueprint, redirect
from flask_login import current_user
from datetime import datetime
from flask_login import login_required
import pytz

from app import login

bp = Blueprint('index', __name__)


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/time', methods=['GET', 'POST'])
@login_required
def time_now():
    return {'time': datetime.now(pytz.timezone('Europe/Madrid')), 'user': current_user.email}


@login.unauthorized_handler     # In unauthorized_handler we have a callback URL
def unauthorized_callback():            # In call back url we can specify where we want to
    return redirect('/register')
