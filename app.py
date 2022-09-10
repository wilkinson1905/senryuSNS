from flask import Flask, url_for, render_template
from flask import session, redirect, request
import json
import sns_db

with open("data/SECRET.json") as f:
    secret_data = json.loads(f.read())

USERLIST = secret_data["user_list"]

def is_login():
    return "login" in session

def get_user():
    if is_login():
        return session["login"]
    return "ゲスト"

def try_login_func(user, password):
    if user not in USERLIST:
        return False
    if USERLIST[user] != password:
        return False
    session["login"] = user
    return True

def show_msg(msg):
    return render_template("msg.html", msg=msg, user=get_user())
def try_logout():
    session.pop("login",None)
    return True

app = Flask(__name__)
app.secret_key = secret_data["secret_key"]

@app.route("/")
def index():
    if not is_login():
        return redirect("/login")
    senryu_list = sns_db.get_all_senryu()
    return render_template("index.html", user=get_user(), senryu_list=senryu_list)

@app.route("/mypage")
def mypage():
    if not is_login():
        return redirect("/login")
    senryu_list = sns_db.get_user_senryu(get_user())
    return render_template("mypage.html", user=get_user(), senryu_list=senryu_list, page_name="マイページ")

@app.route("/delete", methods=['POST'])
def delete_senryu():
    if not is_login():
        return redirect("/login")
    id = request.form.get("id", "")
    user = get_user()
    if id !="":
        sns_db.delete_senryu(id, user)
    return redirect("/mypage")

@app.route("/create_senryu")
def create_senryu():
    if not is_login():
        return redirect("/login")
    return render_template("create.html",user=get_user())

@app.route("/post_senryu", methods=['POST'])
def post_senryu():
    if not is_login():
        return redirect("/login")
    senryu = request.form.get("senryu", "")
    user = get_user()
    sns_db.post_a_senryu(user, senryu)
    return show_msg("川柳を投稿しました")


@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/try_login", methods=['POST'])
def try_login():
    user = request.form.get("user", "")
    pw = request.form.get("pw","")
    if try_login_func(user,pw):
        return redirect("/")
    return show_msg("ログインに失敗しました")
@app.route("/logout")
def logout():
    try_logout()
    return show_msg("ログアウトしました")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")