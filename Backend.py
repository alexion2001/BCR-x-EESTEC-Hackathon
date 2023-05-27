from flask import Flask, jsonify, request
from calcul_sume import sume as sume_calculate

app = Flask(__name__)

@app.route('/income', methods=['GET'])
def get_income():
    return jsonify({'income': sume_calculate['venituri']})

@app.route('/food', methods=['GET'])
def get_food():
    return jsonify({'food': sume_calculate['mancare']})

@app.route('/household', methods=['GET'])
def get_household():
    return jsonify({'household': sume_calculate['casa']})

@app.route('/transport', methods=['GET'])
def get_transport():
    return jsonify({'transport': sume_calculate['transport']})

@app.route('/others', methods=['GET'])
def get_others():
    return jsonify({'others': sume_calculate['diverse']})

if __name__ == '__main__':
    app.run()