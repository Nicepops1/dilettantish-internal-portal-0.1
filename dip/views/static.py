import pathlib

from flask import Blueprint, current_app, send_from_directory, send_file
from dip.models import User


bp = Blueprint('static', __name__)


@bp.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


@bp.route(f'/user/<id_>/photo')
def send_user_image(id_):

    user = User.query.filter_by(id=id_).first()

    filename = user.photo

    filepath = pathlib.Path(current_app.root_path).parent / current_app.config["PATHS"]["user_images"] / filename

    return send_file(filepath)