from flask import Flask

app = Flask(__name__)


@app.route("/")
def header():
    return (f"<h1>{name}</h1>")

if __name__ == '__main__':
    app.run(debug=True)

