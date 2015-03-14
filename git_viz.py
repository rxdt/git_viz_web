from flask import Flask, request, render_template
from flask import render_template_string
import os

app = Flask(__name__)
app.config.from_object(__name__)




@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':

        if request.form['submit'] == 'commit1':
            os.system('/Users/rxdt/git_viz_unity/or_demo_mac.app/Contents/MacOS/or_demo_mac')
            return render_template('index.html')

        # elif request.form['submit'] == 'commit1':
            # os.system('/Users/rxdt/git_viz_unity/or_demo_mac.app/Contents/MacOS/or_demo_mac')
            # return render_template('index.html')
            
        else:
            pass 

    elif request.method == 'GET':
        return render_template('index.html')

    


if __name__ == '__main__':
    app.run(debug=True)