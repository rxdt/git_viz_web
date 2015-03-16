from flask import Flask, request, render_template
from flask import render_template_string
import os

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/rails')
def rails():
    os.system('static/gitviz_rails.app/Contents/MacOS/gitviz_rails')
    return render_template('index.html')

@app.route('/flask')
def flask():
    os.system('static/gitviz_small_flask.app/Contents/MacOS/gitviz_small_flask')
    return render_template('index.html')

@app.route('/git_viz_this')
def git_viz_this():
    os.system('static/git_viz_this.app/Contents/MacOS/git_viz_this')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)