# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# IMPORTS
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
from flask import Flask, render_template

app = Flask(__name__)



# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# FUNCTIONS
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=



# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# ROUTES
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# @app.route('/')
# def myBasePage():
#     title = "Jacob Clouse Portfolio Website"
#     return render_template('base.html',html_title = title)

    # Index page
@app.route('/')
def myIndexPage():
    title = "Index - Jacob Clouse Portfolio Website"
    return render_template('index.html',html_title = title)


@app.route('/project/<int:projNum>')
def myProjectPage(projNum):
    title = f"Project {projNum} - Jacob Clouse Portfolio Website"
    return render_template('portfolioItemTemplate.html',html_title = title)

# main statement - used to set dev mode
if __name__ == '__main__':
    app.run(debug=True)