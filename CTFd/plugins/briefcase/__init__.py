from flask import render_template
from flask import request
from flask import jsonify

from CTFd.models import db
from CTFd.utils import admins_only, is_admin

from CTFd import utils

def load(app):
    @app.route('/briefcase-verify', methods=['GET'])
    def verify_pin():
	#return render_template('page.html', content="<h1>Briefcase Page</h1>")
        pin = request.args.get('pin', '')
        print(pin)
	if pin == '666':
	    return jsonify(text='You successfully open the briefcase and find this photograph inside. Use the combination 666 as the key for this challenge!', url='https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/articles/health_tools/taking_care_of_kitten_slideshow/photolibrary_rf_photo_of_kitten_sleeping.jpg')
	else: 
	    return jsonify(text="That combination doesn't work. Try again.", url='https://ctf.holyokecodes.org/files/4e984630004c0f23edde27210860030f/locked.jpg')
