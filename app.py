from flask import Flask, render_template, request, session, make_response
from controller import UserController
from controller import RentController
from controller import LessorController
from controller import DealsController
from controller import StuffController
from flask_session import Session
from model.entity import Deals

UPLOAD_FOLDER = "./view/assets/"
ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif"}

app = Flask(__name__, template_folder="view", static_folder="view/assets")
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

SESSION_PERMANENT = 30
app.config["SESSION_TYPE"] = "filesystem"

Session(app)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    try:
        if request.method == "POST":
            status, user = UserController.save(
                request.form.get("name"),
                request.form.get("family"),
                request.form.get("gender"),
                request.form.get("birth_date"),
                request.form.get("email"),
                request.form.get("city"),
                request.form.get("address"),
                request.form.get("phone"),
                request.form.get("username"),
                request.form.get("password"),
                True,
                request.form.get("user_id"),
                request.form.get("image")
            )

            if status:
                file = request.files["file"]
                filename = f"{UPLOAD_FOLDER}user_image/{user.id}.{file.filename.split('.')[-1]}"
                file.save(filename)
                user.image = filename.replace(UPLOAD_FOLDER, "")
                UserController.edit_image(user)
            return render_template("index.html", user=user)
        return render_template("signup.html")

    except Exception as e:
        return render_template("error.html", error=str(e))


# app = Flask(__name__, template_folder="view", static_folder="view/assets")
# Session(app)


@app.route('/')
def homepage():  # put application's id here
    return render_template("index.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    try:
        if request.method == "POST":
            status, data = UserController.find_by_user_password(
                request.form.get("username"),
                request.form.get("password")
            )

            if status:
                session["user"] = data
                return render_template("index.html", user=session["user"])
        return render_template("login.html")

    except Exception as e:
        return render_template("error.html", error=str(e))


@app.route('/stuff', methods=["GET", "POST"])
def stuff():
    try:
        if request.method == "POST":
            status, stuff = StuffController.save(
                request.form.get("car_name"),
                request.form.get("color"),
                request.form.get("brand"),
                request.form.get("year"),
                request.form.get("price"),
                request.form.get("information"),
                request.form.get("car_image"),
                True

            )

            if status:
                file = request.files["file"]
                filename = f"{UPLOAD_FOLDER}car_image/{stuff.id}.{file.filename.split('.')[-1]}"
                file.save(filename)
                stuff.car_image = filename.replace(UPLOAD_FOLDER, "")
                StuffController.edit_car_image(stuff)
            return render_template("index.html", user=session.get("user"))
        return render_template("stuff.html", stuff_list=StuffController.find_all()[1], user=session.get("user"))

    except Exception as e:
        return render_template("error.html", error=str(e))


@app.route('/deal', methods=["GET", "POST"])
def deal():
    try:
        if request.method == "POST":
            DealsController.save(
                request.form.get("name"),
                request.form.get("family"),
                request.form.get("gender"),
                request.form.get("birth_date"),
                request.form.get("email"),
                request.form.get("city"),
                request.form.get("address"),
                request.form.get("phone"),
                request.form.get("username"),
                request.form.get("password"),
                request.form.get("user_id"),
                request.form.get("image"),
                request.form.get("car_name"),
                request.form.get("color"),
                request.form.get("brand"),
                request.form.get("year"),
                request.form.get("price"),
                request.form.get("information"),
                request.form.get("car_image"),
                request.form.get("role"),
                request.form.get("date"),
                True
            )
        return render_template("deal.html", stuff_list=StuffController.find_all()[1], user_list = UserController.find_all()[1], user=session.get("user"))



    except Exception as e:
        return render_template("error.html", error=str(e))


@app.route("/all-deals")
def deals():
    print(session.get("username"))
    return render_template("deal_tbl.html", deal_list=DealsController.find_all()[1], user=session.get("user"))


@app.route('/renter', methods=["GET", "POST"])
def renter():
    if request.method == "POST":
        RentController.save(
            request.form.get("name"),
            request.form.get("color"),
            request.form.get("brand"),
            request.form.get("year"),
            request.form.get("city"),
            request.form.get("car_id"),
            request.form.get("renter_id"),
            request.form.get("sender_id"),
            request.form.get("rent_date"),
            request.form.get("return_date"),
            request.form.get("rent_price"),
            request.form.get("information"),
            True
        )
    return render_template("renter.html", user=session.get("user"))


@app.route('/lessor', methods=["GET", "POST"])
def lessor():
    if request.method == "POST":
        LessorController.save(
            request.form.get("name"),
            request.form.get("color"),
            request.form.get("brand"),
            request.form.get("year"),
            request.form.get("city"),
            request.form.get("car_id"),
            request.form.get("renter_id"),
            request.form.get("sender_id"),
            request.form.get("rent_date"),
            request.form.get("return_date"),
            request.form.get("rent_price"),
            request.form.get("information"),
            True
        )
    return render_template("lessor_tbl.html", less_list=LessorController.find_all()[1], user=session.get("user"))


@app.route("/user", methods=["GET", "POST"])
def user():
    print(session.get("user"))
    user = None
    if request.method == "POST":
        user = UserController.save(
            request.form.get("name"),
            request.form.get("family"),
            request.form.get("username"),
            request.form.get("password")
        )
    return render_template("signup.html", user_list=UserController.find_all()[1], user=session.get("user"))

    # return render_template("lessor.html", rent_list=RentController.find_all()[1])


if __name__ == "__main__":
    app.run(debug=True)
