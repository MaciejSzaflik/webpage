from random import seed
from random import randint
from flask import Blueprint, request, jsonify

dice = Blueprint('dice', __name__)
seed()

@dice.route("/dice")
def diceRoll():
    side = request.args.get('side', default = 8, type = int)
    count = request.args.get('count', default = 1, type = int)
    sum = 0
    results = []
    for i in range(count):
      rand = randint(1, side)
      results.append(rand)
      sum = sum + rand
    
    toReturn = { 'sum' : sum, 'results' : results }
    return jsonify(toReturn)