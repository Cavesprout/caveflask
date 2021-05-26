from flask import Flask

app = Flask(__name__)

@app.route(request)
def index():
    return render(request, "index.html")

@app.route("/test")
def test_page():
    return "<p>Hello World!</p>"