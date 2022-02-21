from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
  
  #### Return a rendered index.html file
  return render_template('index.html')

@app.route("/blog/")
def blog(id):
    
  #### Return a rendered fried_egg.html file
  return render_template('home_blog.html')