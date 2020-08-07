from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    doc = {
        'order_name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'phone_number': phone_receive
    }

    # print(doc)
    db.shoppingmall.insert_one(doc)

    return jsonify({'result': 'success','msg':'성공적으로 등록되었습니다.'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    shoppings = list(db.shoppingmall.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'shoppings': shoppings})


if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)
