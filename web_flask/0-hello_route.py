#!/usr/bin/python3
""" Will start a flask web application """


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ will display a message """
    return 'Hello HBNB!'

if __name__ == "__main__":
    """ function of the main """
    app.run(host='0.0.0.0', port=5000)
