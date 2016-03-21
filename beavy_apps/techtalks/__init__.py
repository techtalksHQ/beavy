from beavy.common.admin_model_view import AdminPolyModelView
from beavy.app import admin, db

from .blueprint import techtalks_bp
from .models import Video  # noqa
from .views import *  # noqa


def init_app(app):

    app.register_blueprint(techtalks_bp)
    admin.add_view(AdminPolyModelView(Video, db.session,
                                      name="Video",
                                      menu_icon_type='glyph',
                                      menu_icon_value='glyphicon-film'))
