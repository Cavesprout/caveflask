from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Index</p>"

@app.route("/test")
def test_page():
    return "<p>Hello World!</p>"