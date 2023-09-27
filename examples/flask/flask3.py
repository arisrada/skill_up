from flask import Flask

app = Flask(__name__)

def display(username):
	return f' {username}'

app.add_url_rule('/user/<username>', 'display', display)

if __name__ == "__main__":
	app.run()