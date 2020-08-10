from flask import Flask


from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)
app.config['SECRET_KEY'] = '096bd5529ba573bca47c1dca999157f4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcr = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

#function name of our route is 'login'

from flask_blog import routes
#this db declared above is an instance of SQLAlchemy class and is the database for our application
#databases structures can be represented through classes and these classes are called models in sqlalchemy
