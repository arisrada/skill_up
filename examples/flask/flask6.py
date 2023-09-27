from flask import Flask, redirect

app = Flask(__name__)


@app.route("/")
def home():
	return redirect("/index")


@app.route("/index")
def display():
	return "iam in redirected page"


app.run()