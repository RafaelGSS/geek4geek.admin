from flask import Flask
from routes import web

from . import base
from . import config


def create_app():
	app = Flask('geek4geek',
	template_folder="src/resources/templates", static_folder="src/resources/static")

	app.config.from_object('src.base.config')
	base.init_app(app)
	
	app.register_blueprint(web.bp)
	
	return app