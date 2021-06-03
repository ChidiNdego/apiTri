from flask import Flask, request, redirect, url_for, flash, jsonify
# import util as util
import csv_util as csv_util

app = Flask(__name__)

@app.route('/recurrentTxns', methods=['GET'])
def RecurrentTxn():
    data = request.args.get('foracid')
    output = csv_util.getResponse(data)
    # print(output)
    return jsonify(output)

@app.route('/cashbacks', methods=['GET'])
def Cashbacks():
    data = request.args.get('cif_id')
    output = csv_util.getCBResponse(data)
    
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)