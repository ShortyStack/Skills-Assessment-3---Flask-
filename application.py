from flask import Flask
from flask import make_response
from flask import render_template
from flask import request

app = Flask(__name__, static_folder='static')


@app.route('/')
def start_here():
    return render_template("/index.html")

@app.route("/application-form")
def fill_out_form():
    return render_template("/application-form.html")

@app.route("/application", methods=["post"])
def show_results():

    firstname = request.form['firstname']
    lastname = request.form['lastname']
    salary = request.form['salary']
    positions = request.form['positions']
    return render_template("/application-response.html",
        firstname = firstname,
        lastname = lastname,
        salary = salary, 
        positions = positions)

# @app.route("/application-response")
# def response_form():
#     Thank_you=request.args.get("application-response.html")




if __name__ == "__main__":
    app.run(debug=True)
    #This allows the webpage to show the error messages for debugging.
    #Turn off when you go to production.
