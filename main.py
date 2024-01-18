from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.json  # POSTで送信されたJSONデータを受け取る例
    print("Received data:", data)
    return "Data received successfully"

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # ポート番号を5001に変更

