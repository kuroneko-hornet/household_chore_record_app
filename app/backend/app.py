import logging
import mimetypes
import os
from pathlib import Path

from quart import (
    Blueprint,
    Quart,
    abort,
    current_app,
    jsonify,
    make_response,
    request,
    send_file,
    send_from_directory,
)
from quart_cors import cors
from core.authentication import AuthenticationHelper

bp = Blueprint("routes", __name__, static_folder="static")
# Fix Windows registry issue with mimetypes
mimetypes.add_type("application/javascript", ".js")
mimetypes.add_type("text/css", ".css")


@bp.route("/")
async def index():
    return await bp.send_static_file("index.html")


# Empty page is recommended for login redirect to work.
# See https://github.com/AzureAD/microsoft-authentication-library-for-js/blob/dev/lib/msal-browser/docs/initialization.md#redirecturi-considerations for more information
@bp.route("/redirect")
async def redirect():
    return ""


@bp.route("/favicon.ico")
async def favicon():
    return await bp.send_static_file("favicon.ico")


@bp.route("/assets/<path:path>")
async def assets(path):
    return await send_from_directory(Path(__file__).resolve().parent / "static" / "assets", path)

# Send MSAL.js settings to the client UI
@bp.route("/auth_setup", methods=["GET"])
def auth_setup():
    auth_helper = AuthenticationHelper(
        search_index="",
        use_authentication=False,
        server_app_id="",
        server_app_secret="",
        client_app_id="",
        tenant_id="",
        require_access_control=False,
        enable_global_documents=False,
        enable_unauthenticated_access=False,
    )
    return jsonify(auth_helper.get_auth_setup_for_client())

def create_app():
    app = Quart(__name__)
    app.register_blueprint(bp)

    # Level should be one of https://docs.python.org/3/library/logging.html#logging-levels
    default_level = "INFO"  # In development, log more verbosely
    if os.getenv("WEBSITE_HOSTNAME"):  # In production, don't log as heavily
        default_level = "WARNING"
    logging.basicConfig(level=os.getenv("APP_LOG_LEVEL", default_level))

    if allowed_origin := os.getenv("ALLOWED_ORIGIN"):
        app.logger.info("CORS enabled for %s", allowed_origin)
        cors(app, allow_origin=allowed_origin, allow_methods=["GET", "POST"])
    return app
