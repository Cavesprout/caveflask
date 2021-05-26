from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index/index.html")

@app.route("/test")
def test_page():
    return "<p>Hello World!</p>"