from flask import *

app = Flask(__name__)

@app.route("/")
def home():
	return "Home"

@app.route("/display/<float:balance>")
def displayFloat(balance):
	return "my bank balance is %f" % balance



app.run(debug = True)