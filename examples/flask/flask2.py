from flask import Flask

app = Flask(__name__)


@app.route("/user/<username>")
def display(username):
    return f'How are you {username}'

@app.route("/")
def index():
	return "Iam an empty routing"

@app.route("/hello")
def hello():
    return "<h1>Hello All</h1>"



if __name__ == "__main__":
   app.run(debug = True)