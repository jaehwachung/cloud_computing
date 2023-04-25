from flask import Flask, render_template, request, flash, redirect, session
from waitress import serve
from knou_shop2.database import db_session
import os
import datetime
from knou_shop2.models import ShopMember, Goods, Basket, Orders, OrdersItem
from sqlalchemy import func
from sqlalchemy.orm.exc import UnmappedInstanceError

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(30)


@app.route("/")
def shop_run():
    # 상품 목록 가져오기
    all_goods = db_session.query(Goods)

    return render_template("index.html", goods=all_goods)


@app.route("/login")
def login_page():
    return render_template("login.html")


@app.route("/login", methods=['post'])
def login_proc():
    # user login
    user = db_session.query(ShopMember).filter(ShopMember.email == request.form.get('email')).first()
    if user:
        if user.password != request.form.get('password'):
            flash("이메일 또는 비밀번호를 확인해주세요")
            return redirect(request.environ['HTTP_REFERER'])
        else:
            session['email'] = user.email
            session['uid'] = user.id
            return redirect("/")
    else:
        flash("이메일 또는 비밀번호를 확인해주세요")
        return redirect(request.environ['HTTP_REFERER'])


@app.route("/logout")
def logout():
    del session["uid"]
    del session["email"]

    return redirect("/")


@app.route("/goods")
def goods_page():
    # 상품 목록 가져오기
    all_goods = db_session.query(Goods)

    return render_template("goods.html", goods=all_goods)


@app.route("/basket")
def basket_page():
    basket_items = db_session.query(Basket)
    
    basket_item_quantity = [item.goods_item.price * item.goods_cnt for item in basket_items]
    total_money = sum(basket_item_quantity)

    return render_template("basket.html", items=basket_items, total_money=total_money)


@app.route("/basket/add", methods=["post"])
def basket_add():
    entry = Basket()
    entry.member = session['uid']
    entry.goods = request.form.get('goods_id')
    entry.goods_cnt = request.form.get('quantity')
    
    db_session.add(entry)
    db_session.commit()

    return redirect("/basket")


@app.route("/basket/update", methods=["post"])
def basket_update():
    req_goods_ids = request.form.getlist('goods_id')
    req_quantity = request.form.getlist('quantity')

    for goods_id, quantity in zip(req_goods_ids, req_quantity):
        basket_item = db_session.query(Basket).filter(Basket.goods == int(goods_id), Basket.member == session["uid"]).first()
        basket_item.goods_cnt = quantity

        db_session.add(basket_item)
    
    db_session.commit()

    return redirect("/basket")


@app.route("/order", methods=["post"])
def goods_order():
    order_item = Orders()
    order_item.order_str_id = "OID" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    order_item.member = session["uid"]
    order_item.order_date = func.now()

    db_session.add(order_item)
    db_session.commit()

    baskets = db_session.query(Basket).filter(Basket.member == session["uid"])
    for basket_item in baskets:
        detail_item = OrdersItem()
        detail_item.goods = basket_item.goods
        detail_item.goods_price = basket_item.goods_item.price
        detail_item.goods_cnt = basket_item.goods_cnt

        db_session.add(detail_item)
        db_session.delete(basket_item)
    
    flash("주문이 완료되었습니다")
    
    db_session.commit()

    return redirect("/basket")


@app.route("/basket/delete", methods=["post"])
def basket_delete():
    goods_id = request.form.get("delete_goods_id")
    
    try:
        basket_item = db_session.query(Basket).filter(Basket.goods == int(goods_id)).first()    
        db_session.delete(basket_item)
    except UnmappedInstanceError as e:
        pass

    db_session.commit()
    
    return redirect("/basket")


@app.route("/join")
def member_join_page():
    return render_template("join.html")


@app.route("/join", methods=["post"])
def member_join():
    user = ShopMember()
    user.name = request.form.get("name")
    user.email = request.form.get("email")
    user.password = request.form.get("password")
    user.post_code = request.form.get("post_code")
    user.address = request.form.get("address")
    user.detail_address = request.form.get("detail_address")
    user.is_admin = 'N'
    user.create_date = func.now()

    db_session.add(user)
    db_session.commit()

    flash("회원 가입되었습니다")

    return redirect("/")


@app.route("/goods/<int:goods_id>")
def goods_view(goods_id):
    # 상품 가져오기
    item = db_session.query(Goods).filter(Goods.id == goods_id).first()
    if not item:
        flash("잘못된 상품 조회입니다")
        return redirect(request.environ['HTTP_REFERER'])

    return render_template("goods_view.html", item=item)


@app.route("/mypage/tracking")
def mypage_tracking():
    return render_template("tracking.html")


@app.teardown_appcontext
def shutdown_session(exception=None):
    if exception:
        db_session.remove()
    else:
        db_session.commit()

if __name__ == "__main__":
    serve(app, listen="*:80") 
    #app.run(host="0.0.0.0", debug=True)
