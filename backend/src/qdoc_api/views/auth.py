import logging

from flask import Blueprint, request, redirect, current_app
from flask_login import login_required, current_user

from qdoc_api import db

from qdoc_api.models import User

# Add logger
logger = logging.getLogger(__name__)
# Config format and stream/file handlers
formatter = logging.Formatter('%(asctime)s| %(levelname)-8s| %(name)-12s| %(message)s')
stream = logging.StreamHandler()
stream.setFormatter(formatter)
# Set log level and add handlers
logger.setLevel(logging.DEBUG)
logger.addHandler(stream)

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/register', methods=['POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/')
    if not request.query_string:
        return 'info not found'
    email = request.args.get('email')
    password = request.args.get('password')
    user = User(email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return redirect('/login')


@auth.route('/get_users', methods=['GET'])
def get_users():
    u = User.query.first()
    return str(u)
