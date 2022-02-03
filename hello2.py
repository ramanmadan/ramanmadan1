from flask import Flask
app=Flask(__name__)

@app.route("/")
def hello():
    return "why Hello world again"

if __name__ == "__main__":
    app.run()