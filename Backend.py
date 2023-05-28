from flask import Flask, jsonify, request
from calcul_sume import sume as sume_calculate, calculProcent

app = Flask(__name__)

@app.route('/titular', methods=['GET'])
def get_titular():
    return jsonify({'titular': 'Cristian Dinu'})

@app.route('/venit', methods=['GET'])
def get_income():
    return jsonify({'venit': sume_calculate[1]})

@app.route('/mancare', methods=['GET'])
def get_food():
    return jsonify({'mancare': calculProcent(2)})

@app.route('/casa', methods=['GET'])
def get_household():
    return jsonify({'casa': calculProcent(3)})

@app.route('/transport', methods=['GET'])
def get_transport():
    return jsonify({'transport': calculProcent(4)})

@app.route('/diverse', methods=['GET'])
def get_others():
    return jsonify({'diverse': calculProcent(5)})

if __name__ == '__main__':
    app.run()