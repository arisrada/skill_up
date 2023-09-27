from flask import *

app = Flask(__name__)

app.secret_key = "abc"


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/login", methods = ['GET', 'POST'])
def login():
  error = None
  if request.method == "POST":
      if request.form['pass'] != "AAA":
         error = "Invalid password"
      else:
          flash("successfully logged in")
          return redirect(url_for("index"))
  return render_template("log.html", error=error) 


app.run()