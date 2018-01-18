from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def root_page():
	return render_template("index.html", 
	gold = 0,
	log = "&nbsp;",
	)

app.run(debug=True)