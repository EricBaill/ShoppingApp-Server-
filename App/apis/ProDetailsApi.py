from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import Productions, ShopCart, db


class ProDetails(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='pro_id', type=int)
        parse = parser.parse_args()
        pro_id = parse.get('pro_id')
        products = Productions.query.filter(Productions.id.__eq__(pro_id)).first()
        if products:
            data = {
                'amount':products.amount,
                'class_id':products.class_id,
                'create_at':products.create_at,
                'description':products.description,
                'icon':products.icon,
                'id':products.id,
                'img':products.img,
                'info':products.info,
                'old_price':products.old_price,
                'origin':products.origin,
                'p_name':products.p_name,
                'price':products.price,
                'sales':products.sales,
                'text1':products.text1,
                'text2':products.text2,
                'unit':products.unit
            }
            return jsonify(data)


class ProDetails1(Resource):
    def get(self,user_id):
        list_ = []
        carts = ShopCart.query.filter(ShopCart.user_id.__eq__(user_id)).all()
        for cart in carts:
            products = Productions.query.filter(Productions.id.__eq__(cart.pro_id)).first()
            data = {
                'amount': cart.amount,
                'class_id': products.class_id,
                'create_at': products.create_at,
                'description': products.description,
                'icon': products.icon,
                'id': products.id,
                'img': products.img,
                'info': products.info,
                'old_price': products.old_price,
                'origin': products.origin,
                'p_name': products.p_name,
                'price': products.price,
                'sales': products.sales,
                'text1': products.text1,
                'text2': products.text2,
                'unit': products.unit
            }
            list_.append(data)
        return jsonify(list_)

class ProDetails2(Resource):
    def get(self,pro_id,user_id):
        cart = ShopCart.query.filter(ShopCart.pro_id.__eq__(pro_id),ShopCart.user_id.__eq__(user_id)).first()
        if cart:
            cart.amount = cart.amount + 1
            db.session.commit()
            data = {
               'amount':cart.amount,
            }
            return jsonify(data)
        else:
            return jsonify([])



class ProDetails3(Resource):
    def get(self,pro_id,user_id):
        cart = ShopCart.query.filter(ShopCart.pro_id.__eq__(pro_id), ShopCart.user_id.__eq__(user_id)).first()
        if cart:
            cart.amount = cart.amount - 1
            db.session.commit()
            if cart.amount == 0:
                db.session.delete(cart)
                db.session.commit()
        else:
            return jsonify({'msg':'暂无信息'})
        return jsonify('ok')