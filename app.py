'''
现在是:2023/5/21 21:45
依然不要忘记
高みを目指すからこそ出会う壁
'''
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!'

@app.route('/api/data', methods=['GET', 'POST'])
def api_data():
    if request.method == 'GET':
        # 处理 GET 请求
        data = {'message': '这是一个 GET 请求'}
        return jsonify(data)
    elif request.method == 'POST':
        # 处理 POST 请求
        content = request.get_json()
        data = {'message': '这是一个 POST 请求', 'received_data': content}
        return jsonify(data)

if __name__ == '__main__':
    app.run()
