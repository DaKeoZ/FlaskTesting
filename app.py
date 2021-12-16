import os
from flask import Flask, render_template, request, jsonify

webapp = Flask(__name__)

from dbcm2 import DBcm
from appconfig import config
from datetime import date


@webapp.get("/")
def home():
    return render_template("home.html", title="Welcome")


@webapp.get("/about")
def about():
    return render_template("about.html", title="About me")


@webapp.get("/cv")
def mycv():
    return render_template("cv.html", title="My CV")


@webapp.get("/technologies")
def defaultTechnology():
    return render_template("technologies.html", title="Computing technologies")


@webapp.get("/technologies/<index>")
def technologies(index):
    return render_template("technologies.html", title="Computing technologies")


@webapp.get("/interests")
def interests():
    return render_template("interests.html", title="Personal interests")


@webapp.get("/comments")
def comments():
    return render_template("comments.html", title="Post your comment")


@webapp.post("/submitted")
def submitted():
    email = request.form["email"]
    comment = request.form["comment"]

    with DBcm.UseDatabase(config) as db:
        SQL = """
            insert into reviews 
            (email, content) 
            values 
            (%s, %s)
        """
        db.execute(SQL, (email, comment))
    return render_template("success.html", title="Comment submitted")


@webapp.get("/reviews")
def getComments():
    with DBcm.UseDatabase(config) as db:
        SQL = """
            select email, content, date 
            from reviews;
        """
        db.execute(SQL)
        data = db.fetchall()
    return render_template("reviews.html", title="Reviews", review=data)


if __name__ == "__main__":
    webapp.run(debug=True)
