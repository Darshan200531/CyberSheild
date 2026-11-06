import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from flask import Flask, jsonify, render_template
from config import Config
from database.db import init_db

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(Config)

    if test_config:
        app.config.update(test_config)

    # Create folders needed by the application.
    Path(app.config["DATABASE_PATH"]).parent.mkdir(parents=True, exist_ok=True)
    log_dir = Path(app.root_path) / "instance"
    log_dir.mkdir(parents=True, exist_ok=True)

    handler = RotatingFileHandler(
        log_dir / "application.log", maxBytes=1_000_000, backupCount=3
    )
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s: %(message)s"
    ))
    if not app.logger.handlers:
        app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)

    with app.app_context():
        init_db(app.config["DATABASE_PATH"])

    @app.route("/")
    def index():
        return render_template("index.html", app_name="CyberShield Mini SIEM")

    @app.route("/health")
    def health():
        app.logger.info("Health endpoint checked")
        return jsonify({
            "status": "healthy",
            "application": "CyberShield Mini SIEM",
            "version": "0.1.0"
        }), 200

    @app.errorhandler(404)
    def not_found(_error):
        return jsonify({"error": "Resource not found"}), 404

    @app.errorhandler(413)
    def file_too_large(_error):
        return jsonify({"error": "Request exceeds configured size limit"}), 413

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
