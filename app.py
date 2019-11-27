from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"

from database import *	

##### Code here ######
@app.route('/')
def homepage():
	return render_template("home.html")

@app.route('/store')
def functionName():
	return render_template("store.html")

@app.route('/cart')
def cartpage():
	return render_template("cart.html")

@app.route('/about')
def aboutpage():
	return render_template("about.html")

@app.route('/login')
def loginpage():
	return render_template("login.html")

#####################


if __name__ == '__main__':
    app.run(debug=True)