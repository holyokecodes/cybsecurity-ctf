from flask import render_template

from CTFd.models import db
from CTFd.utils import admins_only, is_admin

from CTFd import utils

def load(app):
    @app.route('/briefcase_pin', methods=['GET'])
    def view_faq():
        return render_template('page.html', content="<h1>Briefcase Page</h1>")
