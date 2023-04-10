from flask import Blueprint, render_template, g



bp = Blueprint('bp_index', __name__)


@bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')