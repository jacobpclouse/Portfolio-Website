# IMPORT STATEMENTS
from flask import Flask, render_template

app = Flask(__name__)


# FUNCTIONS


# ROUTES
@app.route('/')
def myIndexPage():
    title = "Jacob Clouse Portfolio Website"
    return render_template('base.html',html_title = title)


# main statement - used to set dev mode
if __name__ == '__main__':
    app.run(debug=True)