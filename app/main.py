from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
   # return 'Home page'
   return render_template("index.html")

@app.route('/about')
def about():
    return 'About page'