from flask import jsonify
from flask_restful import Resource

from App.models import User, db, ShopCart, Orders, Address


class GetUser(Resource):
    def get(self):
        users = User.query.all()
        list_ = []
        if users:
            for user in users:
                data = {
                    'id': user.id,
                    'phone': user.phone,
                }
                list_.append(data)
            return jsonify(list_)
        else:
            return jsonify([])


class delUser(Resource):
    def delete(self ,id):
        user = User.query.filter(User.id==id).first()
        if user:
            carts = ShopCart.query.filter(ShopCart.user_id == user.id).all()
            orders = Orders.query.filter(Orders.user_id == user.id).all()
            adds = Address.query.filter(Address.user_id == user.id).all()
            if carts:
                for cart in carts:
                    db.session.delete(cart)
            else:
                pass
            if orders:
                for order in orders:
                    db.session.delete(order)
            else:
                pass
            if adds:
                for add in adds:
                    db.session.delete(add)
            else:
                pass
            db.session.delete(user)
            db.session.commit()
            return jsonify({'msg': '删除成功！'})
        else:
            return jsonify({})
