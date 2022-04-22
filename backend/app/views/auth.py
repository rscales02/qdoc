import logging
from sqlite3 import IntegrityError
import flask_sqlalchemy

import flask
from flask import Blueprint, request, redirect, url_for, jsonify, make_response
from flask_jwt_extended import get_jwt_identity, create_access_token, verify_jwt_in_request
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
        logger.info('Missing Email/Password')
        return 'Missing Email/Password', 400
    email, password = request_helper(request)
    try:
        user = User(email=email)
    except IntegrityError as e:
        logger.info(e)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    # logger.info('registration successful')
    return redirect(url_for('auth.login')), 200


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if not request.query_string:
        return {}, 400
    email, password = request_helper(request)
    user = User.query.filter_by(email=email).first()
    check_pass = user.check_password(password)
    if not user or not check_pass:
        return 'Wrong username or password', 401
    resp = make_response(redirect(url_for('index.time')), 200)
    token = create_access_token(identity=user.email)
    resp.headers['Authorization'] = 'Bearer %s' % token
    logger.info('Login successful')
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
