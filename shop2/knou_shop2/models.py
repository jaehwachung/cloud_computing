from sqlalchemy import Column, Integer, String, CHAR, DateTime, ForeignKey, Identity
from sqlalchemy.orm import relationship
from knou_shop2.database import Base

class ShopMember(Base):
    __tablename__ = 'shop_member'

    id = Column(Integer, Identity(start=1), primary_key=True)
    name = Column(String(50))
    email = Column(String(200), unique=True)
    password = Column(String(32))
    post_code = Column(String(5))
    address = Column(String(255))
    detail_address = Column(String(255))
    is_admin = Column(CHAR(1))
    create_date = Column(DateTime)

class Goods(Base):
    __tablename__ = 'goods'

    id = Column(Integer, Identity(start=1), primary_key=True)
    goods_name = Column(String(255))
    price = Column(Integer)
    goods_photo = Column(String(255))
    goods_cnt = Column(Integer)
    goods_ranking = Column(Integer)
    goods_description = Column(String(None))

class Orders(Base):
    __tablename__ = 'orders'

    id = Column(Integer, Identity(start=1), primary_key=True)
    order_str_id = Column(String(100))
    member = Column(Integer, ForeignKey('shop_member.id'))
    order_date = Column(DateTime)

class OrdersItem(Base):
    __tablename__ ='orders_item'

    id = Column(Integer, Identity(start=1), primary_key=True)
    goods = Column(Integer, ForeignKey('goods.id'))
    goods_price = Column(Integer)
    goods_cnt = Column(Integer)

class GoodsTracking(Base):
    __tablename__ = 'goods_tracking'

    id = Column(Integer, Identity(start=1), primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    delivery_start_date = Column(DateTime)
    delivery_end_date = Column(DateTime)
    tracking_number = Column(String(50))
    tracking_status = Column(String(30))

class Basket(Base):
    __tablename__ = 'basket'

    id = Column(Integer, Identity(start=1), primary_key=True)
    member = Column(Integer, ForeignKey('shop_member.id'))
    goods = Column(Integer, ForeignKey('goods.id'))
    goods_item = relationship("Goods")
    goods_cnt = Column(Integer)
