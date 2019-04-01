# -*- coding: utf-8 -*-
import time

from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import Orders, Productions, db, Address


class addOrder_(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='user_id', type=int)
        parser.add_argument(name='products', type=str)
        parser.add_argument(name='address_id', type=int)
        parser.add_argument(name='sumprice', type=float)
        parse = parser.parse_args()
        user_id = parse.get('user_id')
        products = parse.get('products')
        address_id = parse.get('address_id')
        sumprice = parse.get('sumprice')
        code = time.time()

        order = Orders()
        order.code = int(code)
        order.user_id = user_id
        order.products = products
        order.address_id = address_id
        order.sumprice = sumprice
        db.session.add(order)
        db.session.commit()
        order_ = Orders.query.order_by(db.desc(Orders.id)).first()
        data = {
            'id':order_.id
        }
        return jsonify(data)


class GetOrder_(Resource):
    def get(self,user_id):
        list_ = []
        orders = Orders.query.filter(Orders.user_id==user_id,Orders.is_remove==0).all()
        if orders:
            for order in orders:
                pros = eval(order.products)
                for i in range(len(pros)):
                    pro_id = pros[i]['id']
                    count = pros[i]['count']
                    pro = Productions.query.filter(Productions.id==pro_id).first()
                    if pro:
                        data = {
                            'order_id':order.id,
                            'status':order.status,
                            'sumprice':order.sumprice,
                            'orderProdArr':{
                                'id':pro.id,
                                'name':pro.name,
                                'price':pro.price,
                                'old_price':pro.old_price,
                                'stock':pro.stock,
                                'title':pro.title,
                                'cover_img':pro.cover_img,
                                'content':pro.content,
                                'counts':count,
                            }
                        }
                    else:
                        pass
                    list_.append(data)
            list2 = []
            for i in range(len(list_)):
                if list_[i] != {}:
                    order_list = []
                    order_list.append(list_[i].get('orderProdArr'))
                    for j in range(i + 1, len(list_)):
                        if list_[i].get('order_id') == list_[j].get('order_id'):
                            order_list.append(list_[j].get('orderProdArr'))
                            list_[i]['orderProdArr'] = order_list
                            list_[j] = {}

                    list2.append(list_[i])
            for k in list2:
                if isinstance(k['orderProdArr'], dict):
                    list_k = []
                    list_k.append(k['orderProdArr'])
                    k['orderProdArr'] = list_k
            return jsonify(list2)
        else:
            return jsonify([])


class GetOrder_01(Resource):
    def get(self,order_id):
        list_ = []
        order = Orders.query.filter(Orders.id==order_id).first()
        if order:
            address = Address.query.filter(Address.id==order.address_id).first()
            pros = eval(order.products)
            for i in range(len(pros)):
                pro_id = pros[i]['id']
                count = pros[i]['count']
                pro = Productions.query.filter(Productions.id == pro_id).first()
                if pro:
                    data = {
                        'order_id': order.id,
                        'status': order.status,
                        'sumprice': order.sumprice,
                        'number': order.code,
                        'create_at': order.create_at.strftime('%Y/%m/%d'),
                        'address':{
                            'id':address.id,
                            'details':address.detail,
                            'isDefault':address.is_default,
                            'phone':address.tel,
                            'receiver':address.linkman
                        },
                        'orderProdArr': {
                            'id': pro.id,
                            'name': pro.name,
                            'price': pro.price,
                            'old_price': pro.old_price,
                            'stock': pro.stock,
                            'title': pro.title,
                            'cover_img': pro.cover_img,
                            'content': pro.content,
                            'counts': count,
                        }
                    }
                else:
                    pass
                list_.append(data)
            list2 = []
            for i in range(len(list_)):
                if list_[i] != {}:
                    order_list = []
                    order_list.append(list_[i].get('orderProdArr'))
                    for j in range(i + 1, len(list_)):
                        if list_[i].get('order_id') == list_[j].get('order_id'):
                            order_list.append(list_[j].get('orderProdArr'))
                            list_[i]['orderProdArr'] = order_list
                            list_[j] = {}

                    list2.append(list_[i])
            for k in list2:
                if isinstance(k['orderProdArr'], dict):
                    list_k = []
                    list_k.append(k['orderProdArr'])
                    k['orderProdArr'] = list_k
            return jsonify(list2)
        else:
            return jsonify([])


class DelOrder_(Resource):
    def delete(self,id):
        order = Orders.query.filter(Orders.id==id).first()
        if order:
            db.session.delete(order)
            db.session.commit()
            return jsonify({'msg':'删除成功'})
        else:
            return jsonify({})

class DelOrder_01(Resource):
    def get(self,order_id):
        order = Orders.query.filter(Orders.id == order_id).first()
        if order:
            order.is_remove = 1
            db.session.commit()
            return jsonify({'msg': '删除成功'})
        else:
            return jsonify({})