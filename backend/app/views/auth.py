import logging

from flask import Blueprint, request, redirect, url_for, jsonify
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
    if verify_jwt_in_request() | get_jwt_identity():
        logger.info('User identified')
        return redirect('/')
    if not request.query_string:
        logger.info('Missing Email/Password')
        return ['Missing Email/Password'], 400
    email = request.args.get('email')
    password = request.args.get('password')
    user = User(email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('auth.login'))


@bp.route('/login', methods=['GET', 'POST'])
def login():
    # if get_jwt_identity():
    #     return redirect(url_for('index'))
    if not request.query_string:
        return {}, 400
    email = request.args.get('email')
    password = request.args.get('password')
    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return 'Wrong username or password', 404
    token = create_access_token(identity=user.email)
    logger.info(token)
    return jsonify(access_token=token)


@bp.route('/get_users', methods=['GET', 'POST'])
def get_users():
    u = User.query.first()
    if not u:
        u = 'Empty DB'
    return jsonify(str(u))
