from flask import Flask, render_template
app = Flask(__name__)


# To use start the server (in terminal):
# export FLASK_APP=server.py
# To change to DEBUG mode, run "export FLASK_ENV=development".
# flask run

# Root route.
@app.route('/')
def hello_world():
    return render_template('./index.html')  # Do not include the parent folder ('template'). Views need to be in templates folder.


# About route.
@app.route('/about')
def about():
    return render_template('./about.html')
