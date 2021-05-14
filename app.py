from flask import Flask, jsonify, request
from workerA import add_nums

app = Flask(__name__)


@app.route("/add")
def add():
    first_num = int(request.args.get('first'))
    second_num = int(request.args.get('second'))
    result = add_nums.delay(first_num, second_num)
    return jsonify({'result': result.get()}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
