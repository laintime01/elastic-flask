from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/search')
def search_autocomplete():
    return "11"

if __name__ == '__main__':
    app.run()
