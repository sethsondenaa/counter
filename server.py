from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "jaosdfuh345nqlkef9l4"

@app.route("/")
def index():
	count = 1
	session["count"] += count
	return render_template("index.html")

@app.route("/plusTwo")
def addTwo():
	session["count"] += 1
	return redirect("/")

@app.route("/reset")
def reset():
	session["count"] = 0
	return redirect("/")

app.run(debug=True)