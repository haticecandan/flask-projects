from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def start_api():  # put application's code here
    if request.method == "POST":
        req_Json = request.json
        name = req_Json["name"]
        return jsonify({"response": "Hello " +name})
    elif request.method == "GET":
        return jsonify({"response": "Get Request Called"})


if __name__ == '__main__':
    app.run()
