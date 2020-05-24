from flask import Flask, render_template
app = Flask(__name__)


# To use start the server (in terminal):
# export FLASK_APP=server.py
# To change to DEBUG mode, run "export FLASK_ENV=development".
# flask run

# Root route.
@app.route('/')
def index():
    return render_template('./index.html')  # Do not include the parent folder ('template'). Views need to be in templates folder.


# About route.
@app.route('/about')
def about():
    return render_template('./about.html')


# Users route.
@app.route('/users/<string:username>')  # Variable rules: To get values from the url, set <variable_name> (in this case, username). In this case type of field has been se tot string.
def users(username=None):
    return render_template('./users.html', name=username)  # It is possible to send variables to the template (in this case, the name of the variable inside the template is name).
