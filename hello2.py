from flask import Flask
app=Flask(__name__)

@app.route("/")
def index():
    return "why Hello world again"

@app.route("/hello")
def hello():
    return "HELLO there"
    
@app.route("/members")
def members():
    return "HELLO there Members"

@app.route("/members/<string:name>/")
def getMember(name):
    return name</string:name>

if __name__ == "__main__":
    app.run()