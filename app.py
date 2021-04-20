from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def handle_home():
    body = request.data # get the request body content
    decored_data = json.loads(body)
    print(decored_data)
    return 'Ok'

if __name__ == '__main__':
    app.run(port=8000, debug=True)