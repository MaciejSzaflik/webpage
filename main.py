from flask import Flask, url_for, render_template, request, Response
from diceRandom import dice

mainApp = Flask(__name__)
mainApp.register_blueprint(dice)

@mainApp.route("/", methods=['GET'])
def home():
    return render_template('/index.html', title="Site")


if __name__ == '__main__':
    mainApp.run()
