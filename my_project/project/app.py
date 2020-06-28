from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           
client = MongoClient('localhost', 27017)  
db = client.dbsparta                      


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/reviews', methods=['POST'])
def write_review():
    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    review_receive = request.form['review_give']

    doc = {
        'title': title_receive,
        'author':author_receive,
        'review':review_receive
    }
    db.bookreview.insert_one(doc)

    return jsonify({'result':'success', 'msg': '맛집평이 잘 저장되었습니다!'})



@app.route('/reviews', methods=['GET'])
def read_reviews():

    reviews = list(db.bookreview.find({},{'_id':0}))    
    return jsonify({'result':'success', 'all_review': reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)