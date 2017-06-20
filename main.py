from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Welcome"

if __name__ == "__main__":
    app.run(debug=True)