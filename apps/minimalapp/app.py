# flaskクラスをimportする
from flask import Flask, current_app, g, render_template, request, url_for

# flaskクラスをインスタンス化する。
app = Flask(__name__)

# URLと実行する関数をマッピングする


@app.route("/")
def index():
    return "hello, Flaskbook!"


@app.route("/hello/<name>", methods=["GET"], endpoint="hello-endpoint")
def hello(name):
    return f"Hello, {name}!"


@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html", name=name)


with app.test_request_context():
    # /
    print(url_for("index"))
    # hello/world
    print(url_for("hello-endpoint", name="world"))
    # name/ichiiro?page=ichiro
    print(url_for("show_name", name="ichiro", page="1"))

# print(current_app)

ctx = app.app_context()
ctx.push()

print(current_app.name)

g.connection = "connection"
print(g.connection)

with app.test_request_context("/user?updated=true"):
    # true
    print(request.args.get("upgrade"))
