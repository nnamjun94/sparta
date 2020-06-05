from pymongo import MongoClient  
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# HTML을 주는 부분


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/order', methods=['POST'])
def write_review():
    # title_receive로 클라이언트가 준 title 가져오기
    title_receive = request.form['title_give']
    print('print-title', title_receive)
    # author_receive로 클라이언트가 준 author 가져오기
    author_receive = request.form['author_give']
    # review_receive로 클라이언트가 준 review 가져오기
    review_receive = request.form['review_give']
    # review_receive로 클라이언트가 준 review 가져오기
    tel_receive = request.form['tel_give']

    # DB에 삽입할 review 만들기
    order = {
        'title': title_receive,
        'author': author_receive,
        'review': review_receive,
        'tel': tel_receive
    }
    # reviews에 review 저장하기
    db.order.insert_one(order)
    # 성공 여부 & 성공 메시지 반환
    return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 작성되었습니다.'})


@app.route('/order', methods=['GET'])
def read_reviews():
    # 1. DB에서 리뷰 정보 모두 가져오기
    order = list(db.order.find({}, {'_id': 0}))
    # 2. 성공 여부 & 리뷰 목록 반환하기
    return jsonify({'result': 'success', 'order': order})


if __name__ == '__main__':
    app.run('localhost', port=3000, debug=True)
