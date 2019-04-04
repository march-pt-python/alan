from flask import Flask, render_template, redirect, request

from mysqlconnection import connectToMySQL


app = Flask(__name__)

# show all of our cats
@app.route("/")
def show_cats():
    print("showing cats")
    db = connectToMySQL('cats')
    print(db)
    query = "SELECT * FROM cats.cats;"
    data = db.query_db(query)
    print(data)
    return render_template("cats.html", data=data)

# create a new cat in the database
@app.route("/createcat", methods=["POST"])
def create_cat():
    print("tried to make a cat")
    print(request.form)
    query_data = {
        'name': request.form['name'],
        'description': request.form['description']
    }
    name = request.form['name']
    query = "INSERT INTO cats (name,description) VALUES ("+name+", %(description)s)"
    db = connectToMySQL('cats')
    db.query_db(query, query_data)
    return redirect("/")


# run our application
if __name__ == "__main__":
    print("running the biz")
    app.run(debug=True)