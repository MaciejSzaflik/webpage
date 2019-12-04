from flask import Flask, url_for, render_template, request, Response

mainApp = Flask(__name__)

@mainApp.route("/", methods=['GET'])
def home():
    return render_template('/index.html', title="Site")

if __name__ == '__main__':
    mainApp.run()
