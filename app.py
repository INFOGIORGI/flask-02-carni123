from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html",titolo="welcome") #nella render template gli posso passare il nome della variabile con il valore assegnato 



@app.route("/aboutus")
def aboutus():
    return render_template("about.html",titolo="About_as")


@app.route("/contact")
def contact():
    return render_template("contact.html",titolo="contact")
app.run(debug=True)