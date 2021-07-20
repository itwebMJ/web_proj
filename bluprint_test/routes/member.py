from flask import Blueprint
bp = Blueprint('member', __name__, url_prefix='/member')

@bp.route('/join')
def join_form():
    return 'join'

@bp.route('/join', methods=['POST'])
def join():
    return 'join'

@bp.route('/login')
def login_form():
    return 'login'

@bp.route('/login', methods=['POST'])
def login():
    return 'login'

