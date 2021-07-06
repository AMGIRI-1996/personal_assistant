from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello from flask."

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=os.getenv('PORT', 1234))