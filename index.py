from flask import Flask, redirect, url_for

# Our Flask app object
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    """Our default routes of '/' and '/index'

    Return: The content we want to display to a user
    """

    return 'index'


@app.route('/<path:path>')
def catch_all(path):
    """A special route that catches all other requests

    Note: Let this be your last route. Priority is defined
    by order, so placing this above other functions will
    cause catch_all() to override then.

    Return: A redirect to our index route
    """

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
