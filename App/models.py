from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#用户表
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # name = db.Column(db.String(128),nullable=False)
    phone = db.Column(db.String(11),nullable=False,unique=True)
    create_at = db.Column(db.DateTime,default=datetime.now())
    # update_at = db.Column(db.DateTime,default=datetime.now(),onupdate=datetime.now())

#管理员表
class Admin(db.Model):
    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128),nullable=False,unique=True)
    phone = db.Column(db.String(11),nullable=False,unique=True)
    pwd = db.Column(db.String(128),nullable=False)
    is_super = db.Column(db.Integer,default=0,nullable=False)
    create_at = db.Column(db.DateTime,default=datetime.now())


#地址表
class Address(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    linkman = db.Column(db.String(64),nullable=False)
    tel = db.Column(db.String(11))
    detail = db.Column(db.String(128))
    is_default = db.Column(db.Integer,default=0,nullable=False)
    status = db.Column(db.Integer,default=0,nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    user = db.relationship('User', primaryjoin='Address.user_id == User.id', backref='address')


#订单表
class Orders(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sumprice = db.Column(db.Float,default=0.0,nullable=False)
    status = db.Column(db.Integer,default=0,nullable=False)
    is_send = db.Column(db.Integer,default=0,nullable=False)
    is_remove = db.Column(db.Integer,default=0,nullable=False)
    code = db.Column(db.String(128),unique=True)
    products = db.Column(db.String(255),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    # pro_id = db.Column(db.Integer, db.ForeignKey('productions.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    create_at = db.Column(db.DateTime, default=datetime.now())


    user = db.relationship('User', primaryjoin='Orders.user_id == User.id', backref='orders')
    # pro = db.relationship('Productions', primaryjoin='Orders.pro_id == Productions.id', backref='orders')
    address = db.relationship('Address', primaryjoin='Orders.address_id == Address.id', backref='orders')



#商品类别表
class ProCls(db.Model):
    __tablename__ = 'procls'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128),nullable=False)
    create_at = db.Column(db.DateTime, default=datetime.now())



#商品表
class Productions(db.Model):
    __tablename__ = 'productions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(256),nullable=False)
    price = db.Column(db.Float,default=0.0,nullable=False)
    old_price = db.Column(db.Float,default=0.0,nullable=False)
    stock = db.Column(db.Integer,default=0,nullable=False)
    commend = db.Column(db.Integer,default=0,nullable=False)
    title = db.Column(db.String(255))
    cover_img = db.Column(db.String(255))
    content = db.Column(db.String(255))
    create_at = db.Column(db.DateTime, default=datetime.now())

    class_id = db.Column(db.Integer, db.ForeignKey('procls.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    class_ = db.relationship('ProCls', primaryjoin='Productions.class_id == ProCls.id', backref='productions')


#购物车
class ShopCart(db.Model):
    __tablename__ = 'shopcart'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.String(255))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    pro_id = db.Column(db.Integer,db.ForeignKey('productions.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    address_id = db.Column(db.Integer,db.ForeignKey('address.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    pro = db.relationship('Productions', primaryjoin='ShopCart.pro_id == Productions.id', backref='shopcart')
    user = db.relationship('User', primaryjoin='ShopCart.user_id == User.id', backref='shopcart')
    address = db.relationship('Address', primaryjoin='ShopCart.address_id == Address.id', backref='shopcart')







#
# #地址表
# class Address(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     user_id = db.Column(db.Integer,db.ForeignKey(User.id, ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
#     desc_id = db.relationship('Desc',backref='address')



#地址：省市区三联表
# class Provinces(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     provinceid = db.Column(db.Integer)
#     province = db.Column(db.String(64))
#     is_default = db.Column(db.Boolean, default=False)
#     province_user = db.relationship('User',backref='provinces',lazy=True)
#     u_pro = db.Column(db.Integer, db.ForeignKey(User.id))
#
# class Cities(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     cityid = db.Column(db.Integer)
#     city = db.Column(db.String(64))
#     provinceid = db.Column(db.Integer)
#     city_pro = db.relationship('Provinces',backref='cities',lazy=True)
#     province_city = db.Column(db.Integer, db.ForeignKey(Provinces.id))
#
# class Areas(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     areaid = db.Column(db.Integer)
#     area = db.Column(db.String(64))
#     cityid = db.Column(db.Integer)
#     detaile = db.Column(db.String(128))
#     area_city = db.relationship('Cities',backref='areas',lazy=True)
#     city_area = db.Column(db.Integer,db.ForeignKey(Cities.id))



#订单商品基本信息
# class Order_detail(db.Model):
#     __tablename__ = 'order_detail'
#
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     price = db.Column(db.Float)
#     amount = db.Column(db.String(126))
#
#     product_id = db.Column(db.Integer, db.ForeignKey('productions.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
#     order_id = db.Column(db.Integer, db.ForeignKey('orders.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
#
#     order = db.relationship('Orders', primaryjoin='Order_detail.order_id == Orders.id', backref='order_detail')
#     product = db.relationship('Productions', primaryjoin='Order_detail.product_id == Productions.id', backref='order_detail')



#订单用户基本信息
# class Order_user(db.Model):
#     __tablename__ = 'order_user'
#
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     d_province = db.Column(db.String(64))
#     d_city = db.Column(db.String(64))
#     d_area = db.Column(db.String(64))
#     d_linkman = db.Column(db.String(64))
#     d_link_phone = db.Column(db.String(64))
#     d_detail = db.Column(db.String(128))
#     is_default = db.Column(db.Boolean,default=False,nullable=False)
#
#     order_id = db.Column(db.Integer, db.ForeignKey('orders.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
#
#     order = db.relationship('Orders', primaryjoin='Order_user.order_id == Orders.id', backref='order_user')
#     user = db.relationship('User', primaryjoin='Order_user.user_id == User.id', backref='order_user')
#

