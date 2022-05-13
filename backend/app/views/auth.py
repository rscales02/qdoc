import logging
from sqlite3 import IntegrityError
import flask_sqlalchemy

import flask
from flask import Blueprint, request, redirect, url_for, jsonify, make_response
from flask_jwt_extended import create_access_token, set_access_cookies
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
    # if verify_jwt_in_request() | get_jwt_identity():
    #     logger.info('User identified')
    #     return redirect('/')
    if not request.query_string:
        return 'Missing Email/Password', 400
    email, password = request_helper(request)
    try:
        user = User(email=email)
    except IntegrityError:
        return 'User already exists', 409
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('auth.login')), 201


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if not request.query_string:
        return {}, 400
    email, password = request_helper(request)
    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return 'Wrong username or password', 401
    resp = make_response(redirect(url_for('index.post')), 200)
    token = create_access_token(identity=user.email)
    set_access_cookies(resp, token)
    return resp


@bp.route('/get_users', methods=['GET', 'POST'])
def get_users():
    u = User.query.all()
    if not u:
        u = 'Empty DB'
    return jsonify(str(u))


def request_helper(req):
    email = req.args.get('email')
    password = req.args.get('password')
    return email, password
