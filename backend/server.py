from flask import Flask

app = Flask(__name__)


@app.route("/api/hello")
def hello():
    return {"message": "Checking the connection"}


if __name__ == "__main__":
    app.run(debug=True)
