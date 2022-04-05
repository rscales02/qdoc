from flask import Blueprint
from datetime import datetime

index = Blueprint('index', __name__)


@index.route('/', methods=['GET', 'POST'])
@index.route('/time', methods=['GET', 'POST'])
def time_now():
    return {'time': datetime.now()}
