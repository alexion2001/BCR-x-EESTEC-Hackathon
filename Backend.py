from flask import Flask, jsonify, request
from calcul_sume import sume as sume_calculate, calculProcent
from calcul_sume import titular,venituri
from flask_cors import CORS
app = Flask(__name__)



CORS(app)

# Your routes and other configurations


@app.route('/titular', methods=['GET'])
def get_titular():
    return jsonify({'titular': titular})

@app.route('/venit', methods=['GET'])
def get_income():
    return jsonify({'venit': sume_calculate[1]})

@app.route('/all', methods=['GET'])
def get_all():
    return jsonify({'mancare': sume_calculate[2],
                    'casa': sume_calculate[3],
                    'transport': sume_calculate[4],
                    'diverse': sume_calculate[5],
                    'venit': venituri,
                    'titular': titular,
                    'mancareProc': calculProcent(2),
                    'casaProc': calculProcent(3),
                    'transportProc': calculProcent(4),
                    })

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