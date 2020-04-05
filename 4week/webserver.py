from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
# 위의 '/'는 url 뒷주소를 의미
def home():
   return render_template("index.html")

@app.route('/mypage')
def my_page():
   return render_template("mypage.html")

@app.route('/shop')
def shop():
   return render_template("shop.html")

#주소 늘어날 때마다 html파일도 하나씩 늘어남

@app.route('/test', methods=["GET"])
def test_get():
   title_receive = request.args.get('title_give') #/test?title-give=123
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 GET!'})

@app.route('/test', methods=["POST"]) #body안에 클라가 {"title_give":123} 보냄
def test_post():
   title_receive = request.form['title_give']
   print(title_receive)
   return jsonify({'result':'success', 'msg': '이 요청은 POST!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)