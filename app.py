
from flask import Flask, render_template, request, jsonify, redirect
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from weather import get_weather

app = Flask(__name__)
app.secret_key = "CHANGE_THIS"

login_manager = LoginManager(app)

USERS = {"owner":{"password":"owner123","role":"owner"}}

class User(UserMixin):
    def __init__(self, u): self.id=u

@login_manager.user_loader
def load(u):
    return User(u) if u in USERS else None

# -------- PUBLIC CHATBOT --------
@app.route("/")
def public_chat():
    return render_template("public.html")

@app.route("/api/public", methods=["POST"])
def public_api():
    text=request.json.get("text","").lower()
    if "ai" in text:
        return jsonify({"reply":"AI helps farmers increase productivity sustainably."})
    return jsonify({"reply":"Hello, I am Kaya, your AgriTech assistant."})

# -------- OWNER SYSTEM --------
@app.route("/owner/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        u=request.form["username"]; p=request.form["password"]
        if u in USERS and USERS[u]["password"]==p:
            login_user(User(u))
            return redirect("/owner")
    return render_template("login.html")

@app.route("/owner")
@login_required
def owner_home():
    return render_template("owner.html")

@app.route("/api/owner", methods=["POST"])
@login_required
def owner_api():
    text=request.json.get("text","").lower()
    if "weather" in text:
        return jsonify({"reply":get_weather("Lusaka")})
    if "bible" in text:
        return jsonify({"reply":"Proverbs 16:3 — Commit thy works unto the LORD."})
    return jsonify({"reply":"Owner mode active."})

@app.route("/owner/logout")
@login_required
def logout():
    logout_user(); return redirect("/")

if __name__=="__main__":
    app.run(debug=True)
