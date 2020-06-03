from flask import Flask, jsonify
import numpy as np
app = Flask(__name__)

@app.route('/det', methods=['POST'])
def detmat():
    n = 100
    m = np.random.rand(n, n)
    det_m =  np.linalg.det(m)
    return jsonify({'result': det_m})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
