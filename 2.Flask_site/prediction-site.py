from flask import Flask, render_template
import pickle


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

app.run(host='0.0.0.0', port=80)