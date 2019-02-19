from flask import jsonify, make_response
from flask_restful import Resource, reqparse, fields, marshal_with

from App.models import Productions, ProductClass, db

pro_fields = {
    'id': fields.Integer,
    'p_name': fields.String,
    'price': fields.Float,
    'old_price': fields.Float,
    'description': fields.String,
    'amount': fields.String,
    'text1': fields.String,
    'text2': fields.String,
    'img': fields.String,
    'icon': fields.String,
    'info': fields.String,
    'unit': fields.String,
    'commend': fields.Integer,
    'sales': fields.String,
    'origin': fields.String,
    'create_at': fields.DateTime,
    'class_id': fields.Integer,
}

pro_class_fields = {
    'class_id': fields.Integer,
    'class_name': fields.String,
}

results_fields = {
    'code': fields.String,
    'message': fields.String,
    'goods': fields.Nested(pro_class_fields),
    'foods': fields.Nested(pro_fields),
}

parser = reqparse.RequestParser()
parser.add_argument(name='name', type=str)
parser.add_argument(name='price', type=float)
parser.add_argument(name='amount', type=str)
parser.add_argument(name='desc', type=str)
# parser.add_argument(name='text1', type=str)
# parser.add_argument(name='text2', type=str)
# parser.add_argument(name='info', type=str)
parser.add_argument(name='img', type=str)
parser.add_argument(name='icon', type=str)
parser.add_argument(name='origin', type=str)
parser.add_argument(name='unit', type=str)
parser.add_argument(name='sales', type=str)
parser.add_argument(name='class_id', type=int)

class AdminPro(Resource):

    def get(self):
        list_ = []
        pros = Productions.query.all()
        if pros:
            for production in pros:
                pro_cls = ProductClass.query.filter(ProductClass.id.__eq__(production.class_id)).first()
                data = {
                    'id':production.id,
                    'p_name':production.p_name,
                    'price':production.price,
                    'old_price':production.old_price,
                    'description':production.description,
                    'amount':production.amount,
                    'img':production.img,
                    'icon':production.icon,
                    'info':production.info,
                    'unit':production.unit,
                    'commend':production.commend,
                    'sales':production.sales,
                    'origin':production.origin,
                    'create_at':production.create_at,
                    'shelf':production.shelf,
                    'cls':pro_cls.class_name,
                }
                list_.append(data)
            return jsonify(list_)
        else:
            return jsonify([])

    @ marshal_with(results_fields)
    def post(self):
        # headers = {
        #     'Content-Type': 'application/json',
        #     'Access-Control-Allow-Origin': '*',
        #     'Access-Control-Allow-Methods': 'POST'
        # }
        parse = parser.parse_args()
        p_name = parse.get('name')
        price = parse.get('price')
        amount = parse.get('amount')
        description = parse.get('desc')
        # text1 = parse.get('text1')
        # text2 = parse.get('text2')
        # info = parse.get('info')
        img = parse.get('img')
        icon = parse.get('icon')
        origin = parse.get('origin')
        unit = parse.get('unit')
        sales = parse.get('sales')
        class_id = parse.get('class_id')
        print(img)
        print(icon)

        pro = Productions()
        pro.p_name = p_name
        pro.price = price
        pro.old_price = price
        pro.amount = amount
        pro.description = description
        # pro.text1 = text1
        # pro.text2 = text2
        # pro.info = info
        pro.img = img
        pro.icon = icon
        pro.origin = origin
        pro.unit = unit
        pro.sales = sales
        pro.class_id = class_id
        db.session.add(pro)
        db.session.commit()

        pro_class = ProductClass.query.filter(ProductClass.id.__eq__(class_id)).first()
        return {'code': '200', 'goods': pro_class, 'foods': pro}
        # return make_response({'code': '200', 'goods': pro_class, 'foods': pro}, 200, headers)


class AdminPro1(Resource):
    def put(self,id):
        # headers = {
        #     'Content-Type': 'application/json',
        #     'Access-Control-Allow-Origin': '*',
        #     'Access-Control-Allow-Methods': 'PUT'
        # }
        list_ = []
        parse = parser.parse_args()
        # p_name = parse.get('name')
        price = parse.get('price')
        # amount = parse.get('amount')
        # description = parse.get('desc')
        # img = parse.get('img')
        # icon = parse.get('icon')
        # origin = parse.get('origin')
        # unit = parse.get('unit')
        # sales = parse.get('sales')
        # class_id = parse.get('class_id')
        production = Productions.query.filter(Productions.id.__eq__(id)).first()
        if production:
            production.old_price = production.price
            # pro.p_name = p_name
            production.price = price
            # pro.amount = amount
            # pro.description = description
            # pro.img = img
            # pro.icon = icon
            # pro.origin = origin
            # pro.unit = unit
            # pro.sales = sales
            # pro.class_id = class_id
            db.session.commit()

            pro_cls = ProductClass.query.filter(ProductClass.id.__eq__(production.class_id)).first()
            data = {
                'id': production.id,
                'p_name': production.p_name,
                'price': production.price,
                'old_price': production.old_price,
                'description': production.description,
                'amount': production.amount,
                'img': production.img,
                'icon': production.icon,
                'info': production.info,
                'unit': production.unit,
                'sales': production.sales,
                'commend': production.commend,
                'origin': production.origin,
                'create_at': production.create_at,
                'cls': pro_cls.class_name,
            }
            list_.append(data)
            return jsonify(list_)
            # return make_response(jsonify(list_), 200, headers)

        else:
            return jsonify([])

    def delete(self,id):
        production = Productions.query.filter(Productions.id.__eq__(id)).first()
        if production:
            db.session.delete(production)
            db.session.commit()
            return jsonify({'msg':'删除成功！'})
        else:
            return jsonify({'msg':'删除失败！'})

class AdminPro2(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='id', type=int)
        parser.add_argument(name='num', type=int)
        parse = parser.parse_args()
        id = parse.get('id')
        num = parse.get('num')

        print(num)

        product = Productions.query.filter(Productions.id.__eq__(id)).first()
        if product:
            product.shelf = num
            db.session.commit()
            return jsonify({'msg':'修改成功！'})
        else:
            return jsonify({'msg':'暂无商品信息！'})
