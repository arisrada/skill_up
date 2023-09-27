from flask import *

app = Flask(__name__)

@app.route("/")
def display():
   return render_template("message.html")


app.run()