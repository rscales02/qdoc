from flask import Blueprint
from datetime import datetime

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
@main.route('/time', methods=['GET', 'POST'])
def index():
    return {'time': datetime.now()}
