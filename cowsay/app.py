#!flask/bin/python
from flask import Flask, jsonify
import subprocess
import sys

app = Flask(__name__)


@app.route('/cowsay/api/v1.0/saysomething', methods=['GET'])
def cow_say():
    data=subprocess.check_output(["cowsay","Hello student"])
    return jsonify({'cow_said':data})

if __name__ == '__main__':
    ip = sys.argv[1]
    app.run(str(ip),debug=True)

