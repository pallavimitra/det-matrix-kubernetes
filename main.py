from flask import Flask
import numpy as np
app = Flask(__name__)

@app.route("/inv")
def invmat():
    n = 100
    m = np.random.rand(n, n)
    inv_m =  np.linalg.inv(m)
    return inv_m

if __name__ == "__main__":
    app.run(host='0.0.0.0')
