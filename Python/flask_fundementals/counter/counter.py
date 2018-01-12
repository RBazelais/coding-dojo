from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = ":)"


@app.route('/')
def index(amount = 0):
    if "count" in session:
        session["count"] += amount
    else:
        session["count"] = 0

    return render_template('index.html')

@app.route('/<amount>')#set route to whatever amount we set
def multiple(amount):
    return index(int(amount))

@app.route('/reset')
def reset():
    session["count"] = 1
    return redirect('/')
app.run(debug=True)
