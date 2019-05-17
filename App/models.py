from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#用户表
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # name = db.Column(db.String(128),nullable=False)
    phone = db.Column(db.String(11),nullable=False,unique=True)
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    # update_at = db.Column(db.DateTime,default=datetime.now(),onupdate=datetime.now())

#管理员表
class Admin(db.Model):
    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account = db.Column(db.String(128),nullable=False)
    pwd = db.Column(db.String(128),nullable=False)
    is_super = db.Column(db.Integer,default=0,nullable=False)
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)


#轮播表
class Carousel(db.Model):
    __tablename__ = 'carousel'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cover_img = db.Column(db.String(255),nullable=False)
    content = db.Column(db.String(255),nullable=False)
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)



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
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)


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
    price = db.Column(db.Float,default=0.0,nullable=False)
    old_price = db.Column(db.Float,default=0.0,nullable=False)
    stock = db.Column(db.Integer,default=0,nullable=False)
    commend = db.Column(db.Integer,default=0,nullable=False)
    title = db.Column(db.String(255))
    cover_img = db.Column(db.String(255),nullable=False)
    content = db.Column(db.String(255))
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

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
