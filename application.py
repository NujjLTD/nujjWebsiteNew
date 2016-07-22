from flask import Flask, render_template, request
from flask.ext.mobility import Mobility
from flask.ext.mobility.decorators import mobile_template

app = Flask(__name__)
app.debug=True

Mobility(app)

@app.route('/')
@app.route('/index')
@mobile_template('{mobile/}index')
def index(template):
    return render_template(template + ".html")


@app.route('/aboutUs')
@mobile_template('{mobile/}aboutUs')
def about(template):
	return render_template(template + ".html")

@app.route('/TermsAndConditions')
def terms():
	return render_template('Terms_and_Conditions.html')

@app.route('/socialMedia')
def temp():
    return render_template('socialMedia.html')

@app.route('/template')
def social():
    return render_template('template.html')

if __name__ == '__main__':
    app.run(host='192.168.0.22', port=5002, threaded=True, debug=True)

