from sqlalchemy import Column, Integer, NVARCHAR, CHAR, DateTime, ForeignKey, NVARCHAR
from sqlalchemy.orm import relationship
from database import Base

class ShopMember(Base):
    __tablename__ = 'shop_member'

    id = Column(Integer, primary_key=True)
    name = Column(NVARCHAR(50))
    email = Column(NVARCHAR(200), unique=True)
    password = Column(NVARCHAR(32))
    post_code = Column(NVARCHAR(5))
    address = Column(NVARCHAR(255))
    detail_address = Column(NVARCHAR(255))
    is_admin = Column(CHAR(1))
    create_date = Column(DateTime)

class Goods(Base):
    __tablename__ = 'goods'

    id = Column(Integer, primary_key=True)
    goods_name = Column(NVARCHAR(255))
    price = Column(Integer)
    goods_photo = Column(NVARCHAR(255))
    goods_cnt = Column(Integer)
    goods_ranking = Column(Integer)
    goods_description = Column(NVARCHAR(None))

class Orders(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    order_str_id = Column(NVARCHAR(100))
    member = Column(Integer, ForeignKey('shop_member.id'))
    order_date = Column(DateTime)

class OrdersItem(Base):
    __tablename__ ='orders_item'

    id = Column(Integer, primary_key=True)
    goods = Column(Integer, ForeignKey('goods.id'))
    goods_price = Column(Integer)
    goods_cnt = Column(Integer)

class GoodsTracking(Base):
    __tablename__ = 'goods_tracking'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    delivery_start_date = Column(DateTime)
    delivery_end_date = Column(DateTime)
    tracking_number = Column(NVARCHAR(50))
    tracking_status = Column(NVARCHAR(30))

class Basket(Base):
    __tablename__ = 'basket'

    id = Column(Integer, primary_key=True)
    member = Column(Integer, ForeignKey('shop_member.id'))
    goods = Column(Integer, ForeignKey('goods.id'))
    goods_item = relationship("Goods")
    goods_cnt = Column(Integer)
