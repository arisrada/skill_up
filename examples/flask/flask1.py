from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
	return "I'm in training"

@app.route("/index")
def index():
	return "INDEX"


if __name__ == "__main__":
	app.run()