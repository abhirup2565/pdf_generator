import os
from flask import Flask
from dotenv import load_dotenv

from app.Blueprints import main_blueprint
from app.Blueprints import user_blueprint
from app.Blueprints import main_blueprint
from app.extension import db,jwt
load_dotenv()

def create_app():
    app=Flask(__name__)
    app.secret_key=os.getenv('secret_key')
    #Loading configs
    app.config.from_prefixed_env()
    #Initializing extensions
    db.init_app(app)
    jwt.init_app(app)
    #Register Blueprint
    app.register_blueprint(main_blueprint) 
    app.register_blueprint(user_blueprint) 
    return app
    
    