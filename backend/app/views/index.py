from flask import Blueprint, redirect, url_for, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, verify_jwt_in_request
from app import jwt
from datetime import datetime
import pytz

from app.models import Post
from app import db

import logging
# Add logger
logger = logging.getLogger(__name__)
# Config format and stream/file handlers
formatter = logging.Formatter('%(asctime)s| %(levelname)-8s| %(name)-12s| %(message)s')
stream = logging.StreamHandler()
stream.setFormatter(formatter)
# Set log level and add handlers
logger.setLevel(logging.DEBUG)
logger.addHandler(stream)

bp = Blueprint('index', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    return {'time': datetime.now(pytz.timezone('Europe/Madrid'))}, 200


@bp.route('/post', methods=['GET', 'POST'])
@jwt_required()
def post():
    current_user = get_jwt_identity()
    logger.info(request.args)
    body = request.args.get('body')
    p = Post(body=body, author=current_user)
    db.session.add(p)
    db.session.commit()
    return {'time': datetime.now(pytz.timezone('Europe/Madrid')), 'user': current_user}, 201


@bp.route('/get_posts', methods=['GET', 'POST'])
def get_posts():
    p = Post.query.all()
    if not p:
        p = 'Empty DB'
    return jsonify(str(p))
