from flask import Flask, render_template, request, jsonify, redirect
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from weather import get_weather
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret")

login_manager = LoginManager(app)
login_manager.login_view = "login"

# ---- USERS ----
USERS = {
    "owner": {
        "password": os.environ.get("OWNER_PASSWORD", "owner123"),
        "role": "owner"
    }
}

class User(UserMixin):
    def __init__(self, username):
        self.id = username

@login_manager.user_loader
def load_user(user_id):
    return User(user_id) if user_id in USERS else None

# ---------------- PUBLIC CHATBOT ----------------

@app.route("/")
def public_chat():
    return render_template("public.html")

@app.route("/api/public", methods=["POST"])
def public_api():
    text = request.json.get("text", "").lower()

    if "ai" in text:
        reply = "AI helps farmers predict yields, manage water, and fight climate change."
    elif "bible" in text:
        reply = "Genesis 2:15 — God put man in the garden to tend and keep it."
    else:
        reply = "Hello, I am Kaya 🌱 Your AgriTech assistant."

    return jsonify({"reply": reply})

# ---------------- OWNER LOGIN ----------------

@app.route("/owner/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = request.form.get("username")
        p = request.form.get("password")

        if u in USERS and USERS[u]["password"] == p:
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
    text = request.json.get("text", "").lower()

    if "weather" in text:
        reply = get_weather("Lusaka")
    elif "bible" in text:
        reply = "Proverbs 16:3 — Commit your work to the Lord."
    else:
        reply = "Owner mode active. Full control enabled."

    return jsonify({"reply": reply})

@app.route("/owner/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run()