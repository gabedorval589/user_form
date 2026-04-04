from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("home.html")

@app.route("/get_user")
def get_user():
    return render_template("form.html")
    


if __name__ == "__main__":
    app.run()