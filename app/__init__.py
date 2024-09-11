from flask import Flask # type: ignore
from app.models import db
from app.config import config_options
from flask_migrate import Migrate # type: ignore
from app.books import book_blueprint
from flask_bootstrap import Bootstrap5 # type: ignore




def create_app(config_name='prd'):
 
 

    app = Flask(__name__)
    current_config = config_options[config_name]
    #print(current_config)
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI
    app.config.from_object(current_config) 

    # Connect db with app
    db.init_app(app)
    
    "add migrate to the project "
    migrate = Migrate(app, db)
    bootstrap = Bootstrap5(app)
    
    app.register_blueprint(book_blueprint)
    
    
    return app
    


 