# ==========================================
# app.py
# Purpose:
# Flask application entrypoint.
#
# Responsibilities:
# - initialize Flask app
# - register blueprints
# - configure template/static folders
# - start Flask server
#
# Why This File Exists:
# Keeps application startup logic separate
# from:
# - routes
# - workflow orchestration
# - business logic
#
# This improves:
# - maintainability
# - scalability
# - production readiness
# ==========================================



# ==========================================
# Flask Imports
# ==========================================

from flask import Flask



# ==========================================
# Route Blueprints
# ==========================================

from backend.app.routes.home_routes import (
    home_blueprint
)



# ==========================================
# Initialize Flask App
# ==========================================

app = Flask(

    __name__,

    template_folder="frontend/templates",

    static_folder="frontend/static"

)



# ==========================================
# Flask Secret Key
# ==========================================

app.secret_key = (
    "resume_match_secret"
)



# ==========================================
# Register Application Routes
# ==========================================

app.register_blueprint(

    home_blueprint

)



# ==========================================
# Run Flask Application
# ==========================================

if __name__ == "__main__":

    app.run(

        debug=True,

        use_reloader=False

    )