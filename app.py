'''
�嶬敲�:2023/5/21 21:45
卆隼音勣梨芝
互みを朕峺すからこそ竃氏う謁
'''
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!'

@app.route('/api/data', methods=['GET', 'POST'])
def api_data():
    if request.method == 'GET':
        # 侃尖 GET 萩箔
        data = {'message': '宸頁匯倖 GET 萩箔'}
        return jsonify(data)
    elif request.method == 'POST':
        # 侃尖 POST 萩箔
        content = request.get_json()
        data = {'message': '宸頁匯倖 POST 萩箔', 'received_data': content}
        return jsonify(data)

if __name__ == '__main__':
    app.run()
