from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def homePage(): 
  return "test"

app.run( host = "0.0.0.0", port = 8765)