from flask import Flask
from config import Config
from app.extensions import db, migrate, jwt

from app.tweet import tweetBp
from app.user import userBp
from app.auth import authBp
from app.postCount import countBp

from datetime import timedelta

from app.models.user import Users
from app.models.tweet import Tweets
from app.models.count_tweet import CountTweets


from flask_admin import Admin
from flask_login import current_user, LoginManager, user_loaded_from_request

from app.admin.MyCustomModel import CustomModelView

import schedule
import time
import threading


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(hours=1)
    app.config.from_object(config_class)

    admin = Admin(name="Admin Panel", template_mode="bootstrap4")


    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)


    @login_manager.user_loader
    def user_loader(user_id):
        user = Users.query.get(int(user_id))
        return user

    def schedule_count_tweets():
        with app.app_context():
            from app.postCount.postCount import count_tweet
            count_tweet()
    
    schedule.every(60).seconds.do(schedule_count_tweets)
    # Start the scheduler in a separate thread
    def run_scheduler():
        while True:
            schedule.run_pending()
            time.sleep(1)

    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.daemon = True
    scheduler_thread.start()
    

    admin.add_view(CustomModelView(Users, db.session))
    admin.add_view(CustomModelView(Tweets, db.session))
    admin.add_view(CustomModelView(CountTweets, db.session))



    app.register_blueprint(countBp, url_prefix='/api/counts')
    app.register_blueprint(tweetBp, url_prefix='/api/tweets')
    app.register_blueprint(userBp, url_prefix='/api/users')
    app.register_blueprint(authBp, url_prefix='/api/auth')

    return app
