import logging

from flask import Blueprint, request, redirect
from flask_login import current_user, login_user

from app import db

from app.models import User

# Add logger
logger = logging.getLogger(__name__)
# Config format and stream/file handlers
formatter = logging.Formatter('%(asctime)s| %(levelname)-8s| %(name)-12s| %(message)s')
stream = logging.StreamHandler()
stream.setFormatter(formatter)
# Set log level and add handlers
logger.setLevel(logging.DEBUG)
logger.addHandler(stream)

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect('/')
    if not request.query_string:
        return 400
    email = request.args.get('email')
    password = request.args.get('password')
    user = User(email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return redirect('/login')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    if not request.query_string:
        return [], 400
    email = request.args.get('email')
    password = request.args.get('password')
    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password_hash(password):
        return redirect('/register')
    login_user(user)
    next_page = request.args.get('next')
    if not next_page:
        next_page = '/time'
    return redirect(next_page)


@bp.route('/get_users', methods=['GET'])
def get_users():
    u = User.query.first()
    return str(u)
