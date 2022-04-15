from flask import Blueprint, redirect, url_for, request
from flask_jwt_extended import jwt_required, get_jwt_identity, verify_jwt_in_request
from app import jwt
from datetime import datetime
import pytz

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
@bp.route('/time', methods=['GET', 'POST'])
@jwt_required()
def time():
    current_user = get_jwt_identity()
    logger.info(request.args)
    return {'time': datetime.now(pytz.timezone('Europe/Madrid')), 'user': current_user}, 200
