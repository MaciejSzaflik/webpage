from flask import Flask
mainApp = Flask(__name__)

@app.route("/")
def hello_www():
    return "Hello World Wide Web!"

if __name__ == '__main__':
    mainApp.run()
