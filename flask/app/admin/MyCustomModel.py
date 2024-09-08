from flask_admin.contrib.sqla import ModelView
from flask import redirect
from flask_admin import AdminIndexView
import os
from dotenv import load_dotenv
from flask_login import current_user


load_dotenv()


BASE_URL = os.getenv("BASE_URL")

class CustomModelView(ModelView):
    print(current_user)
    def is_accessible(self):
        return current_user.is_authenticated and current_user.has_role("user")

    def inaccessible_callback(self, name, **kwargs):
        return redirect(f"{BASE_URL}/login")