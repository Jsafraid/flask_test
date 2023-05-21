'''
������:2023/5/21 21:45
��Ȼ��Ҫ����
�ߤߤ�Ŀָ�����餳�����ᤦ��
'''
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!'

@app.route('/api/data', methods=['GET', 'POST'])
def api_data():
    if request.method == 'GET':
        # ���� GET ����
        data = {'message': '����һ�� GET ����'}
        return jsonify(data)
    elif request.method == 'POST':
        # ���� POST ����
        content = request.get_json()
        data = {'message': '����һ�� POST ����', 'received_data': content}
        return jsonify(data)

if __name__ == '__main__':
    app.run()
