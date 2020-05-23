from flask import Flask
app = Flask(__name__)


# To use start the server (in terminal):
# export FLASK_APP=server.py
# flask run
# To change to DEBUG mode, run "FLASK_ENV=development" and then "flask run".

# Root route.
@app.route('/')
def hello_world():
    return 'Hello, World! :)'
