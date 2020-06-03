from flask import Flask, jsonify
import numpy as np
app = Flask(__name__)

@app.route('/inv', methods=['POST'])
def invmat():
    n = 100
    m = np.random.rand(n, n)
    inv_m =  np.linalg.det(m)
    return jsonify({'result': inv_m})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
