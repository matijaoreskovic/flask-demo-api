from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=["GET"])
def testGet():
    return 'This is a test message!'

@app.route('/', methods=["POST"])
def testPost():
     input_json = request.get_json(force=True) 
     dictToReturn = {'text':input_json['text']}
     return jsonify(dictToReturn)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8084)