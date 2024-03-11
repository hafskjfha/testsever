from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/need_data')
def provide_data():
    # 간단한 JSON 데이터 생성
    data = {
        "message": "This is a simple JSON response from the server!",
        "number": 42
    }
    # JSON 형식으로 데이터를 클라이언트에게 반환
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
