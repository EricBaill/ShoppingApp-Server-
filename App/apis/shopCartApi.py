# -*- coding: utf-8 -*-
from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import ShopCart, db, Productions


class ShopCart_(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='user_id', type=int)
        parser.add_argument(name='pro_id', type=int)
        parser.add_argument(name='address_id', type=int)
        parser.add_argument(name='number', type=str)
        parse = parser.parse_args()
        user_id = parse.get('user_id')
        pro_id = parse.get('pro_id')
        address_id = parse.get('address_id')
        number = parse.get('number')
        cart = ShopCart()
        cart.user_id = user_id
        cart.pro_id = pro_id
        cart.address_id = address_id
        cart.number = number
        db.session.add(cart)
        db.session.commit()

        cart = ShopCart.query.order_by(db.desc(ShopCart.id)).first()
        production = Productions.query.filter(Productions.id == cart.pro_id).first()
        if production:
            data = {
                'cart_id': cart.id,
                'id': production.id,
                'price': production.price,
                'stock': production.stock,
                'title': production.title,
                'cover_img': production.cover_img,
                'number': int(cart.number)
            }
            return jsonify(data)
        else:
            return jsonify({})


class GetShopCart(Resource):
    def get(self,user_id):
        list_ = []
        carts = ShopCart.query.filter(ShopCart.user_id==user_id).all()
        if carts:
            for cart in carts:
                production = Productions.query.filter(Productions.id==cart.pro_id).first()
                if production:
                    data = {
                        'cart_id':cart.id,
                        'id': production.id,
                        'price': production.price,
                        'stock': production.stock,
                        'title': production.title,
                        'cover_img': production.cover_img,
                        'number':int(cart.number)
                    }
                    list_.append(data)
                else:
                    pass
            return jsonify(list_)
        else:
            return jsonify([])


class DelShopCart(Resource):
    def delete(self,user_id,id):
        cart = ShopCart.query.filter(ShopCart.user_id==user_id,ShopCart.id==id).first()
        if cart:
            db.session.delete(cart)
            db.session.commit()
            return jsonify({'msg':'删除成功！'})
        else:
            return jsonify({})


class AddShopCart(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='user_id', type=int)
        parser.add_argument(name='id', type=int)
        parser.add_argument(name='number', type=int)
        parse = parser.parse_args()
        user_id = parse.get('user_id')
        id = parse.get('id')
        number = parse.get('number')
        cart = ShopCart.query.filter(ShopCart.user_id==user_id,ShopCart.id==id).first()
        if cart:
            cart.number = int(cart.number)+int(number)
            print(cart.number)
            db.session.commit()
            return jsonify({'msg':'添加成功'})
        else:
            return jsonify({})


class CutShopCart(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='user_id', type=int)
        parser.add_argument(name='id', type=int)
        parser.add_argument(name='number', type=int)
        parse = parser.parse_args()
        user_id = parse.get('user_id')
        id = parse.get('id')
        number = parse.get('number')
        cart = ShopCart.query.filter(ShopCart.user_id==user_id,ShopCart.id==id).first()
        if cart:
            cart.number = int(cart.number)-int(number)
            db.session.commit()
            return jsonify({'msg':'添加成功'})
        else:
            return jsonify({})
