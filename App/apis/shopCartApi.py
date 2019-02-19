from flask import jsonify, make_response
from flask_restful import reqparse, Resource
from App.models import Productions, db, ShopCart


class ShopCartResource(Resource):
    def get(self):
        pros = Productions.query.filter(Productions.id==Productions.user_id).all()
        if pros:
            return {'code': '200', 'foods': pros}
        else:
            return {'code': '404', 'message': '您的购物车目前是空的！'}


    def post(self):
        headers = {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST'
        }
        parser = reqparse.RequestParser()
        parser.add_argument(name='user_id', type=int)
        parser.add_argument(name='pro_id', type=int)
        parser.add_argument(name='amount', type=int)
        parse = parser.parse_args()
        user_id = parse.get('user_id')
        pro_id = parse.get('pro_id')
        amount = parse.get('amount')
        cart = ShopCart()
        cart.user_id = user_id
        cart.pro_id = pro_id
        cart.amount = amount
        try:
            db.session.add(cart)
            db.session.commit()
        except Exception as e:
            print(str(e))
        # return jsonify({'msg':'添加成功！'})
        return make_response((jsonify({'msg':'添加成功！'}), 200, headers))




