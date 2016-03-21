from flask import Blueprint

techtalks_bp = Blueprint('techtalks', __name__,
                         template_folder='templates')
