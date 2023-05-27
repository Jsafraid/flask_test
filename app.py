# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 模拟保存数据的变量
data = None

@app.route('/')
def index():
    return "hello flask!"

@app.route('/api/data', methods=['GET', 'POST'])
def api_data():
    global data

    if request.method == 'GET':
        # 处理 GET 请求，返回保存的数据
        response = {'data': data}
        return jsonify(response)
    elif request.method == 'POST':
        # 处理 POST 请求，接收数据并保存
        content = request.get_json()
        data = content['data']

        # 返回成功的响应
        response = {'status': 'success'}
        return jsonify(response)

@app.route('/api/control', methods=['POST'])
def api_control():
    # 处理控制命令
    content = request.get_json()
    command = content['command']

    # 执行相应的控制操作
    # ...

    # 返回成功的响应
    response = {'status': 'success'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
