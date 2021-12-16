import os
from flask import Flask, render_template, request

webapp = Flask(__name__)
numTechnologies = 0
currentTechnology = 1


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
    """return technologies(1)"""
    return render_template("technologies.html", title="Computing technologies")


@webapp.get("/technologies/<index>")
def technologies(index):
    """currentTechnology = int(index)
    if (int(index) > numTechnologies): index = numTechnologies
    s = "technologies{id}.html"
    return render_template(s.format(id=index), title="Computing technologies")"""
    return render_template("technologies.html", title="Computing technologies")


@webapp.get("/interests")
def interests():
    return render_template("interests.html", title="Personal interests")


@webapp.get("/comments")
def comments():
    return render_template("comments.html", title="Comments")


@webapp.post("/submitted")
def submitted():
    email = request.form["email"]
    comment = request.form["comment"]
    with open("./static/resources/comments.txt", "a") as sf:
        print(f"{email}\n{comment}\n", file=sf)
    return render_template("success.html", title="Comment submitted")


"""def previousTechnology():
    return

@webapp.post("/next")
def nextTechnology():
    s = "technologies{id}.html"
    return render_template(s.format(id=currentTechnology+1), title="Computing technologies")"""

if __name__ == "__main__":
    files = os.listdir("./templates")
    for file in files:
        if file.startswith("technologies"):
            numTechnologies += 1
    webapp.run(debug=True)
