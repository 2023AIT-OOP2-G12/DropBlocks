from flask import Flask, request

app = Flask(__name__)

@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.json  # POSTで送信されたJSONデータを受け取る例
    print("Received data:", data)
    return "Data received successfully"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
