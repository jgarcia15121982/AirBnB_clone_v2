#!/usr/bin/python3
""" Will start a flask web application """


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ will display a message """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ will display hbnb """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ display C with the value of text """
    return 'C ' + text.replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """ display python with the value of text """
    return 'Python ' + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ if n is an integer return a message """
    return ("{:d} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def html(n):
    """ display a html if n is an integer """
    return render_template('5-number.html', value=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """  display a html if n is an integer """
    return render_template('6-number_odd_or_even.html', value=n)


if __name__ == "__main__":
    """ function of the main """
    app.run(host='0.0.0.0', port=5000)
