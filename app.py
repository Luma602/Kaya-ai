import os
from flask import Flask, render_template, request, jsonify
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    login_required,
    logout_user,
)

from weather import get_weather

# ---------------- APP SETUP ----------------
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# ---------------- USERS (TEMP – OWNER ONLY) ----------------
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
    if user_id in USERS:
        return User(user_id)
    return None

# ---------------- PUBLIC CHATBOT ----------------
@app.route("/")
def public_chat():
    return render_template("public.html")

@app.route("/api/public", methods=["POST"])
def public_api():
    message = request.json.get("message", "")
    return jsonify({
        "reply": f"Kaya says: I received your message -> {message}"
    })

# ---------------- OWNER LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = USERS.get(username)
        if user and user["password"] == password:
            login_user(User