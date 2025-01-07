from flask import Flask, render_template
import pickle


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
    # return 'hello world!'

app.run(host='0.0.0.0', port=80)