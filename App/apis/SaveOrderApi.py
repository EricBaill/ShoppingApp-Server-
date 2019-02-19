from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import Orders, db

parser = reqparse.RequestParser()
parser.add_argument(name='id',type=int,required=True,help='用户id不能为空')
parser.add_argument(name='address_id',type=int)
parser.add_argument(name='p_name',type=str)
parser.add_argument(name='price',type=float)
parser.add_argument(name='d_code',type=str)

class SaveOrder(Resource):
    def post(self):
        parse = parser.parse_args()
        id = parse.get('id')
        p_name = parse.get('p_name')
        price = parse.get('price')
        d_code = parse.get('d_code')
        address_id = parse.get('address_id')

        order = Orders()
        order.user_id = id
        order.d_code = d_code
        order.order_pro = p_name
        order.desc_id = address_id
        order.sumprice = price
        db.session.add(order)
        db.session.commit()

        return jsonify({'msg':'订单保存成功！'})

