from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


#用户表
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(11),nullable=False,unique=True)
    head_img = db.Column(db.String(255),nullable=False,default='http://soft1906.xin/head_img.jpeg')
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

#=管理员表
class Admin(db.Model):
    __tablename__ = 'admin'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128),nullable=False,unique=True)
    phone = db.Column(db.String(11),nullable=False,unique=True)
    pwd = db.Column(db.String(128),nullable=False)
    is_super = db.Column(db.Integer,default=0,nullable=False)
    create_at = db.Column(db.DateTime,nullable=False, default=datetime.now)
    update_at = db.Column(db.DateTime,nullable=False, default=datetime.now,onupdate=datetime.now())


#地址表
class Desc(db.Model):
    __tablename__ = 'desc'

    id = db.Column(db.Integer, primary_key=True)
    province = db.Column(db.String(64),nullable=False)
    city = db.Column(db.String(64),nullable=False)
    area = db.Column(db.String(64),nullable=False)
    linkman = db.Column(db.String(64),nullable=False)
    link_phone = db.Column(db.String(64))
    detail = db.Column(db.String(128))
    is_default = db.Column(db.Boolean,default=False,nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    user = db.relationship('User', primaryjoin='Desc.user_id == User.id', backref='desc')




#订单表
class Orders(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean,default=False,nullable=False)
    is_send = db.Column(db.Integer,default=0,nullable=False)
    is_receive = db.Column(db.Integer,default=0,nullable=False)
    d_code = db.Column(db.String(128),unique=True)
    order_pro = db.Column(db.String(256))
    sumprice = db.Column(db.Float,nullable=False)

    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    update_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now())

    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    desc_id = db.Column(db.Integer, db.ForeignKey('desc.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    user = db.relationship('User', primaryjoin='Orders.user_id == User.id', backref='orders')
    desc = db.relationship('Desc', primaryjoin='Orders.desc_id == Desc.id', backref='orders')




#商品类别表
class ProductClass(db.Model):
    __tablename__ = 'product_class'

    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(128),nullable=False)
    create_at = db.Column(db.DateTime,nullable=False, default=datetime.now)
    update_at = db.Column(db.DateTime,nullable=False, default=datetime.now,onupdate=datetime.now)



#商品表
class Productions(db.Model):
    __tablename__ = 'productions'

    id = db.Column(db.Integer, primary_key=True)
    p_name = db.Column(db.String(256),nullable=False)
    price = db.Column(db.Float,nullable=False)
    old_price = db.Column(db.Float,nullable=False)
    description = db.Column(db.String(64),nullable=False)
    amount = db.Column(db.String(64),default=1,nullable=False)
    text1 = db.Column(db.String(128))
    text2 = db.Column(db.String(128))
    img = db.Column(db.Text,nullable=False)
    icon = db.Column(db.Text,nullable=False)
    info = db.Column(db.String(256))
    unit = db.Column(db.String(128))
    sales = db.Column(db.String(128))
    origin = db.Column(db.String(128))
    shelf = db.Column(db.Integer,default=0,nullable=False)
    commend = db.Column(db.Integer,default=0,nullable=False)
    create_at = db.Column(db.DateTime,nullable=False, default=datetime.now)
    update_at = db.Column(db.DateTime,nullable=False, default=datetime.now,onupdate=datetime.now)

    class_id = db.Column(db.Integer, db.ForeignKey('product_class.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    class_ = db.relationship('ProductClass', primaryjoin='Productions.class_id == ProductClass.id', backref='productions')




#订单商品基本信息
# class Order_detail(db.Model):
#     __tablename__ = 'order_detail'
#
#     id = db.Column(db.Integer, primary_key=True)
#     price = db.Column(db.Float,nullable=False)
#     amount = db.Column(db.String(126),nullable=False)
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
#     id = db.Column(db.Integer, primary_key=True)
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




#购物车
class ShopCart(db.Model):
    __tablename__ = 'shopcart'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer,default=0,nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    pro_id = db.Column(db.Integer,db.ForeignKey('productions.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    order = db.relationship('Productions', primaryjoin='ShopCart.pro_id == Productions.id', backref='shopcart')
    user = db.relationship('User', primaryjoin='ShopCart.user_id == User.id', backref='shopcart')



