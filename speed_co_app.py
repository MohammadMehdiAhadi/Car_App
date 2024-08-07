from flask import Flask, request, render_template

from controller.user_controller import UserController

app = Flask(__name__, template_folder="view", static_folder="view/assets")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("signup.html")


@app.route("/signup")
def signup():
    print(request.args.get("name"))
    print(request.args.get("role"))
    UserController.save()

app.run()
