from flask import Flask, render_template
from waitress import serve

app = Flask(__name__)

@app.route("/")
def shop_run():
    return render_template("index.html")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/goods")
def goods_page():
    return render_template("goods.html")

@app.route("/basket")
def basket_page():
    return render_template("basket.html")

@app.route("/join")
def member_join_page():
    return render_template("join.html")

@app.route("/goods/<goods_id>")
def goods_view(goods_id):
    return render_template("goods_view.html")

@app.route("/mypage/tracking")
def mypage_tracking():
    return render_template("tracking.html")

if __name__ == "__main__":
    serve(app, listen="*:80")
    #app.run(host="0.0.0.0", debug=True)
