import os
import redis
from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from raven.contrib.flask import Sentry

# Initialize App
app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_APP_SECRET_KEY")

# Initialize Sentry
sentry = Sentry(app)

#Initialize database connection
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
db = SQLAlchemy(app)

#Initialize migration libary
migrate = Migrate(app, db)

#Initialize Bcrypt
bcrypt = Bcrypt(app)

#Initialize flask_login
login_manager = LoginManager()
login_manager.init_app(app)

from .models.auth import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


#Initialize redis cache
cache = redis.StrictRedis.from_url((os.environ.get("REDIS_URL")))

#Access/API tokens configured here
app.config["GITHUB_ACCESS_TOKEN"] = os.environ.get("GITHUB_TOKEN")
app.config["MAILGUN_DOMAIN"] = os.environ.get("MAILGUN_DOMAIN")
app.config["MAILGUN_API_KEY"] = os.environ.get("MAILGUN_API_KEY")

# Import and Initialize blueprints
from blog.models.post import BlogPost
from blog.home.views import home_blueprint
from blog.view.views import view_blueprint
from blog.create.views import create_blueprint
from blog.api.v1.views import api_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(view_blueprint, url_prefix='/blog')
app.register_blueprint(create_blueprint, url_prefix='/create')
app.register_blueprint(api_blueprint, url_prefix='/api/v1')


# Import error handlers
from blog import errorhandlers