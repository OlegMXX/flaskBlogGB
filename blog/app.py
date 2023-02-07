import os
from flask import Flask, render_template
from blog.models.database import db
from blog.views.users import users_app
from blog.views.articles import articles_app
from blog.views.auth import login_manager, auth_app
from blog.views.authors import authors_app
from flask_migrate import Migrate
from blog.security import flask_bcrypt
from blog.admin import admin
from blog.api import init_api

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


# Blueprints
app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")
app.register_blueprint(authors_app, url_prefix="/authors")

# Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////home/olly/Рабочий стол/flaskBasics/flaskProjectGB/blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Auth app
app.config["SECRET_KEY"] = "1%uwf1khz)wwf0(cve_@&ms7y!2g#reilnuy+*a_q1%!^g(z^f"
app.register_blueprint(auth_app, url_prefix="/auth")
login_manager.init_app(app)

# Configurations
cfg_name = os.environ.get("CONFIG_NAME") or "DevConfig"
app.config.from_object(f"blog.configs.{cfg_name}")

# Migrations
migrate = Migrate(app, db, compare_type=True)

# Security
flask_bcrypt.init_app(app)

# Flask-Admin
admin.init_app(app)

# API
api = init_api(app)
