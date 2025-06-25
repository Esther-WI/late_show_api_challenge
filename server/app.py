from flask import Flask
from server.config import create_app, db
from server.models import *
from server.controllers.guest_controller import guest_bp
from server.controllers.episode_controller import episode_bp
from server.controllers.appearance_controller import appearance_bp
from server.controllers.auth_controller import auth_bp

app = create_app()

app.register_blueprint(guest_bp)
app.register_blueprint(episode_bp)
app.register_blueprint(appearance_bp)
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True)
