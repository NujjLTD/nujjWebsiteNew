from flask import Flask, render_template, request
from flask.ext.mobility import Mobility
from flask.ext.mobility.decorators import mobile_template

application = Flask(__name__)
application.debug=True

Mobility(application)

@application.route('/')
@application.route('/index')
@mobile_template('{mobile/}index')
def index(template):
    return render_template(template + ".html")


@application.route('/aboutUs')
@mobile_template('{mobile/}aboutUs')
def about(template):
	return render_template(template + ".html")

@application.route('/TermsAndConditions')
def terms():
	return render_template('Terms_and_Conditions.html')

@application.route('/socialMedia')
def temp():
    return render_template('socialMedia.html')

@application.route('/template')
def social():
    return render_template('template.html')

if __name__ == '__main__':
    application.run()

