import datetime

from flask import jsonify
from flask_restful import reqparse, Resource, fields, marshal_with
from sqlalchemy import and_, extract

from App.models import db, Orders, Productions, Desc

parser = reqparse.RequestParser()

parser.add_argument(name='id',type=int,required=True,help='用户id不能为空')
parser.add_argument(name='phone',type=str,required=True,help='手机号不能为空')
parser.add_argument(name='name',type=str,required=True,help='用户名不能为空')
parser.add_argument(name='status',type=bool,required=True,help='请填写订单状态')
parser.add_argument(name='p_name',type=str,required=True,help='商品名不能为空')
parser.add_argument(name='price',type=float)
parser.add_argument(name='amount',type=str,required=True,help='商品数量不能为空')
parser.add_argument(name='province',type=str,required=True,help='省份不能为空')
parser.add_argument(name='city',type=str,required=True,help='城市不能为空')
parser.add_argument(name='area',type=str,required=True,help='地区不能为空')
parser.add_argument(name='detail',type=str)
parser.add_argument(name='d_linkman',type=str)
parser.add_argument(name='d_link_phone',type=str)
parser.add_argument(name='d_icon',type=str)
parser.add_argument(name='is_default',type=bool)



order_fields = {
    'id':fields.Integer,
    'pro_name':fields.String,
    'price':fields.Float,
    'amount':fields.String,
    'icon':fields.String,
}
results_fields = {
    'code': fields.String,
    'message': fields.String,
    'orders': fields.Nested(order_fields),
}

class OrderResource(Resource):
    def get(self,user_id):
        orders = Orders.query.filter(Orders.user_id==user_id).all()
        list_ = []
        for order in orders:
            for op in eval(order.order_pro):
                amount = op['amount']
                desc = Desc.query.filter(Desc.id == order.desc_id).first()
                pros = Productions.query.filter(Productions.id.__eq__(op['pid'])).all()
                for pro in pros:

                    data = {
                        'user_id':user_id,
                        'order_id':order.id,
                        'd_code': order.d_code,
                        'd_status':order.status,
                        'is_send':order.is_send,
                        'is_receive':order.is_receive,
                        'd_province': desc.province,
                        'd_city': desc.city,
                        'd_area': desc.area,
                        'd_linkman': desc.linkman,
                        'd_link_phone': desc.link_phone,
                        # 'd_detail': desc.d_detail,
                        'order':{
                            'id':pro.id,
                            'pro_name':pro.p_name,
                            'price':pro.price,
                            'amount':amount,
                            'icon':pro.icon,
                        }
                }
                list_.append(data)
        list2 = []
        for i in range(len(list_)):
            if list_[i] != {}:
                order_list = []
                order_list.append(list_[i].get('order'))
                for j in range(i + 1, len(list_)):
                    if list_[i].get('order_id') == list_[j].get('order_id'):
                        order_list.append(list_[j].get('order'))
                        list_[i]['order'] = order_list
                        list_[j] = {}
                # list2.append(list_[i])
                if type(list_[i]['order']) == list:
                    pass
                else:
                    list_[i]['order'] = [list_[i]['order']]
                list2.append(list_[i])
        if list2:
            return jsonify(list2)
        else:
            data = {
                'code':404,
                'msg':'暂无订单信息！'
            }
            return jsonify(data)


class OrderResource1(Resource):
    @marshal_with(results_fields)
    def put(self,order_id):
        order = Orders.query.filter(Orders.id==order_id).first()
        if order:
            order.status = True
            try:
                db.session.commit()
            except Exception as e:
                print(str(e))
            return {'message':'订单修改成功！'}
        else:
            return {'message':'订单修改失败！'}


class OrderResource2(Resource):
    def get(self):
        orders = Orders.query.filter(Orders.status==False).all()
        list_ = []
        for order in orders:
            for op in eval(order.order_pro):
                amount = op['amount']
                desc = Desc.query.filter(Desc.id == order.desc_id).first()
                pros = Productions.query.filter(Productions.id.__eq__(op['pid'])).all()
                for pro in pros:

                    data = {
                        'user_id':order.user_id,
                        'order_id':order.id,
                        'd_code': order.d_code,
                        'd_status':order.status,
                        'd_province': desc.province,
                        'd_city': desc.city,
                        'd_area': desc.area,
                        'd_linkman': desc.linkman,
                        'd_link_phone': desc.link_phone,
                        'sumprice':order.sumprice,
                        # 'd_detail': desc.d_detail,
                        'order':{
                            'id':pro.id,
                            'pro_name':pro.p_name,
                            'price':pro.price,
                            'amount':amount,
                            'icon':pro.icon,
                        }
                }
                list_.append(data)

        list2 = []
        for i in range(len(list_)):
            if list_[i] != {}:
                order_list = []
                order_list.append(list_[i].get('order'))
                for j in range(i + 1, len(list_)):
                    if list_[i].get('order_id') == list_[j].get('order_id'):
                        order_list.append(list_[j].get('order'))
                        list_[i]['order'] = order_list
                        list_[j] = {}
                # list2.append(list_[i])
                if type(list_[i]['order']) == list:
                    pass
                else:
                    list_[i]['order'] = [list_[i]['order']]
                list2.append(list_[i])
        if list2:
            return jsonify(list2)
        else:
            data = {
                'code':404,
                'msg':'暂无订单信息！'
            }
            return jsonify(data)


class OrderResource3(Resource):
    def get(self):

        years = datetime.datetime.now().strftime('%Y')
        months = datetime.datetime.now().strftime('%m')
        days = datetime.datetime.now().strftime('%d')

        orders = Orders.query.filter(and_(
                extract('year',Orders.create_at) == years,
                extract('month',Orders.create_at) == months,
                extract('day',Orders.create_at) == days
            )).all()
        list_ = []

        for order in orders:
            for op in eval(order.order_pro):
                amount = op['amount']
                desc = Desc.query.filter(Desc.id == order.desc_id).first()
                pros = Productions.query.filter(Productions.id.__eq__(op['pid'])).all()
                for pro in pros:
                    data = {
                        'user_id':order.user_id,
                        'order_id':order.id,
                        'd_code': order.d_code,
                        'd_status':order.status,
                        'is_send': order.is_send,
                        'd_province': desc.province,
                        'is_receive': order.is_receive,
                        'd_city': desc.city,
                        'd_area': desc.area,
                        'd_linkman': desc.linkman,
                        'd_link_phone': desc.link_phone,
                        'd_detail': desc.detail,
                        'price': order.sumprice,
                        'order':{
                            'id':pro.id,
                            'pro_name':pro.p_name,
                            'price':pro.price,
                            'amount':amount,
                            'icon':pro.icon,
                        }
                    }
                    list_.append(data)
        list2 = []
        for i in range(len(list_)):
            if list_[i] != {}:
                re_list = []
                re_list.append(list_[i].get('order'))
                for j in range(i + 1, len(list_)):
                    if list_[i].get('order_id') == list_[j].get('order_id'):
                        re_list.append(list_[j].get('order'))
                        list_[i]['order'] = re_list
                        list_[j] = {}
                if type(list_[i]['order']) == list:
                    pass
                else:
                    list_[i]['order'] = [list_[i]['order']]
                list2.append(list_[i])
        return jsonify(list2)


class OrderResource4(Resource):
    def get(self):
        years = datetime.datetime.now().strftime('%Y')
        months = datetime.datetime.now().strftime('%m')

        orders = Orders.query.filter(and_(
            extract('year', Orders.create_at) == years,
            extract('month', Orders.create_at) == months,
        )).all()
        list_ = []
        for order in orders:
            for op in eval(order.order_pro):
                amount = op['amount']
                desc = Desc.query.filter(Desc.id == order.desc_id).first()
                pros = Productions.query.filter(Productions.id.__eq__(op['pid'])).all()
                for pro in pros:
                    data = {
                        'user_id':order.user_id,
                        'order_id':order.id,
                        'd_code': order.d_code,
                        'd_status':order.status,
                        'is_send': order.is_send,
                        'd_province': desc.province,
                        'd_city': desc.city,
                        'd_area': desc.area,
                        'd_linkman': desc.linkman,
                        'd_link_phone': desc.link_phone,
                        'd_detail': desc.detail,
                        'price': order.sumprice,
                        'order':{
                            'id':pro.id,
                            'pro_name':pro.p_name,
                            'price':pro.price,
                            'amount':amount,
                            'icon':pro.icon,
                        }
                    }
                    list_.append(data)
        list2 = []
        for i in range(len(list_)):
            if list_[i] != {}:
                re_list = []
                re_list.append(list_[i].get('order'))
                for j in range(i + 1, len(list_)):
                    if list_[i].get('order_id') == list_[j].get('order_id'):
                        re_list.append(list_[j].get('order'))
                        list_[i]['order'] = re_list
                        list_[j] = {}
                if type(list_[i]['order']) == list:
                    pass
                else:
                    list_[i]['order'] = [list_[i]['order']]
                list2.append(list_[i])
        return jsonify(list2)

class OrderResource5(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='id', type=int)
        parser.add_argument(name='num', type=int)
        parse = parser.parse_args()
        id = parse.get('id')
        num = parse.get('num')
        print(num)
        order = Orders.query.filter(Orders.id.__eq__(id)).first()
        if order:
            order.is_send = num
            db.session.commit()
            return jsonify({'msg':'修改成功！'})
        else:
            return jsonify({'msg':'暂无信息！'})

