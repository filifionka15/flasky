import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_pagedown import PageDown


basedir = os.path.abspath(os.path.dirname(__file__))

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
pagedown = PageDown()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    #config[config_name].init_app(app)
    
    '''app.config['SECRET_KEY'] = 'hard to guess string'
    app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
    app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')
    app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
    app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <flasky@example.com>' 
    app.config['FLASKY_POSTS_PER_PAGE'] = 20
    app.config['FLASKY_FOLLOWERS_PER_PAGE'] = 50
    app.config['FLASKY_COMMENTS_PER_PAGE'] = 30
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False '''
    
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')


    # здесь выполняется подключение маршрутов и
    # нестандартных страниц с сообщениями об ошибках
    return app