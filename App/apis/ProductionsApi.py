from flask import jsonify
from flask_restful import reqparse, Resource, fields, marshal_with
from App.models import Productions, db, ProductClass

parser = reqparse.RequestParser()
parser.add_argument(name='class_name',type=str,required=True,help='商品类名不能为空')
parser.add_argument(name='p_name',type=str,required=True,help='商品名不能为空')
parser.add_argument(name='price',type=float)
parser.add_argument(name='old_price',type=float)
parser.add_argument(name='amount',type=str)
parser.add_argument(name='description',type=str)
parser.add_argument(name='text1',type=str)
parser.add_argument(name='text2',type=str)
parser.add_argument(name='info',type=str)
parser.add_argument(name='img',type=str)
parser.add_argument(name='icon',type=str)
parser.add_argument(name='origin',type=str)
parser.add_argument(name='unit',type=str)
parser.add_argument(name='sales',type=str)
parser.add_argument(name='class_id',type=int)

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
    'commend': fields.Integer,
    'unit': fields.String,
    'sales': fields.String,
    'origin': fields.String,
    'create_at': fields.DateTime,
    'class_id': fields.Integer,
}

pro_class_fields = {
    'class_id': fields.Integer,
    'class_name': fields.String,
    # 'foods': fields.List(fields.Nested(pro_fields)),
}

results_fields = {
    'code': fields.String,
    'message': fields.String,
    'goods': fields.Nested(pro_class_fields),
    'foods': fields.Nested(pro_fields),
}

class ProductinsResource(Resource):
    def get(self):
        pro_classes = ProductClass.query.filter(ProductClass.id == Productions.class_id).all()
        productions = Productions.query.filter(Productions.class_id == ProductClass.id).all()
        list_ = []
        for pro_class in pro_classes:
            for production in productions:
                if production.class_id == pro_class.id:
                    data = {
                        'class_id':pro_class.id,
                        'class_name':pro_class.class_name,
                        'foods':{
                            'id':production.id,
                            'p_name':production.p_name,
                            'price':production.price,
                            'old_price':production.old_price,
                            'description':production.description,
                            'amount':production.amount,
                            'text1':production.text1,
                            'text2':production.text2,
                            'img':production.img,
                            'icon':production.icon,
                            'info':production.info,
                            'unit':production.unit,
                            'sales':production.sales,
                            'commend':production.commend,
                            'origin':production.origin,
                            'create_at':production.create_at,
                            'class_id':production.class_id,
                        }
                    }
                    list_.append(data)
        list2 = []
        for i in range(len(list_)):
            if list_[i] != {}:
                order_list = []
                order_list.append(list_[i].get('foods'))
                for j in range(i+1,len(list_)):
                    if list_[i].get('class_id') == list_[j].get('class_id'):
                        order_list.append(list_[j].get('foods'))
                        list_[i]['foods'] = order_list
                        list_[j] = {}

                list2.append(list_[i])
        for k in list2:
            if isinstance(k['foods'], dict):
                list_k = []
                list_k.append(k['foods'])
                k['foods'] = list_k
        return jsonify(list2)


    @ marshal_with(results_fields)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='name', type=str, required=True, help='商品名不能为空')
        parser.add_argument(name='price', type=float)
        parser.add_argument(name='amount', type=str)
        parser.add_argument(name='desc', type=str)
        # parser.add_argument(name='text1', type=str)
        # parser.add_argument(name='text2', type=str)
        parser.add_argument(name='price', type=float)
        parser.add_argument(name='img', type=str)
        parser.add_argument(name='icon', type=str)
        parser.add_argument(name='origin', type=str)
        parser.add_argument(name='unit', type=str)
        parser.add_argument(name='sales', type=str)
        parser.add_argument(name='class_id', type=int)
        parse = parser.parse_args()
        p_name = parse.get('name')
        price = parse.get('price')
        old_price = parse.get('price')
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

        pro = Productions()
        pro.p_name = p_name
        pro.price = price
        pro.old_price = old_price
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
        try:
            db.session.add(pro)
            db.session.commit()
        except Exception as e:
            print(str(e))

        pro_class = ProductClass.query.filter(ProductClass.id.__eq__(class_id)).first()
        return {'code': '200', 'goods': pro_class, 'foods': pro}



class ProductinsResource1(Resource):
    @marshal_with(results_fields)
    def put(self,production_id):
        productions = Productions.query.all()
        for pro in productions:
            if production_id == pro.id:
                parse = parser.parse_args()
                class_name = parse.get('class_name')
                p_name = parse.get('p_name')
                price = parse.get('price')
                old_price = parse.get('old_price')
                amount = parse.get('amount')
                description = parse.get('description')
                text1 = parse.get('text1')
                text2 = parse.get('text2')
                info = parse.get('info')
                img = parse.get('img')
                icon = parse.get('icon')
                origin = parse.get('origin')
                unit = parse.get('unit')
                sales = parse.get('sales')
                class_id = parse.get('class_id')
                pro.p_name = p_name
                pro.price = price
                pro.old_price = old_price
                pro.amount = amount
                pro.description = description
                pro.text1 = text1
                pro.text2 = text2
                pro.info = info
                pro.img = img
                pro.icon = icon
                pro.origin = origin
                pro.unit = unit
                pro.sales = sales
                pro.class_id = class_id
                pro_class = ProductClass()
                pro_class.class_name = class_name
                try:
                    db.session.add_all([pro,pro_class])
                    db.session.commit()
                except Exception as e:
                    print(str(e))
                    return {'code': '403', 'message': '您修改的商品信息有误，请重新修改！'}
                return {'code': '200', 'goods': pro_class, 'foods': pro}



