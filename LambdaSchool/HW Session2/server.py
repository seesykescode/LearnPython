from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/birthday")
def birthday():
     return "April 29th 1986"

@app.route("/greeting/<name>")
def greeting(name):
    return ("Hello " + name)

@app.route("/sum/<int:p1>/<int:p2>")
def sum(p1, p2):
    return str(p1 + p2)

@app.route("/multiply/<int:p1>/<int:p2>")
def multiply(p1, p2):
    return str(p1 * p2)

@app.route("/subtract/<int:p1>/<int:p2>")
def subtract(p1, p2):
    return str(p1 - p2)


@app.route("/favoritefoods")
def favoritefoods():
     my_list = ['Quest Protein Bars', 'In and Out 4x4 Protein Style', 'Troli Sour Egg Bites', 'Sushi']
     return jsonify(my_list)
