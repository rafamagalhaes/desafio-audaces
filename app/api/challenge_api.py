from flask import Blueprint

version = 'v1'
challenge_blueprint = Blueprint('challenge_blueprint', __name__)


@challenge_blueprint.route(f'/{version}/challenge')
def index():
    return "Challenge accepted"
