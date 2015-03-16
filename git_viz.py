from flask import Flask, request, render_template
from flask import render_template_string
import os

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/index', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        
        if request.form['submit'] == 'rails':
            os.system('static/gitviz_rails.app/Contents/MacOS/gitviz_rails')
            return render_template('index.html')

        elif request.form['submit'] == 'flask':
            os.system('static/gitviz_small_flask.app/Contents/MacOS/gitviz_small_flask')
            return render_template('index.html')

        elif request.form['submit'] == 'this':
            os.system('static/git_viz_this.app/Contents/MacOS/git_viz_this')
            return render_template('index.html')
            
        else:
            pass 

    elif request.method == 'GET':
        return render_template('index.html')

    


if __name__ == '__main__':
    app.run(debug=True)