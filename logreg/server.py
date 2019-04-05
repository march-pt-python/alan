from flask import Flask, render_template, redirect, request, flash
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = "somenonsense"

@app.route("/")
def logreg():
    print("Hit main route")
    return render_template("logreg.html")

@app.route("/success")
def success():
    print("going to success")
    return render_template("success.html")

@app.route("/register", methods=["POST"])
def register():
    error_messages = []
    # is our data valid?    
    # print(request.form)
    if len(request.form["name"])==0:
        print("invalid length")
        error_messages.append("Need a Name!")
    # yes->send it to db
        # success
    # no -> redirect and let users know its bad
        # - flash messages
    if len(error_messages)==0:
        query = "INSERT INTO logreg.users (name, password) VALUES (%(name)s, %(password)s);"
        data = {
            "name": request.form['name'],
            "password": request.form['password']
        }
        db = connectToMySQL("logreg")
        result = db.query_db(query, data)
        return redirect("/success")
    else:
        for message in error_messages:
            flash(message)
        return redirect("/")

@app.route("/login", methods=["POST"])
def login():
    print("logining")
    user_name = request.form['name']
    query = "SELECT * FROM logreg.users WHERE name = '"+user_name+"';"
    data = {"name":user_name}
    db = connectToMySQL("logreg")
    data = db.query_db(query)
    print(data)
    
    return redirect("/success")

if __name__ == "__main__":
    print("Running App!")
    app.run(debug=True)