from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/index')
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/market')
def market():
    return render_template("market.html")

@app.route('/activity')
def activity():
    return render_template("activity.html")

@app.route('/community')
def community():
    return render_template("community.html")

@app.route('/wallet')
def wallet():
    return render_template("wallet.html")
