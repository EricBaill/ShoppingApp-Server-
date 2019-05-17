# -*- coding: utf-8 -*-
from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import ProCls, db, Productions, ShopCart

parser = reqparse.RequestParser()

parser.add_argument(name='name', type=str)


class ProductionCls(Resource):
    def get(self):
        list_ = []
        proclss = ProCls.query.all()
        if proclss:
            for procls in proclss:
                data = {
                    'id':procls.id,
                    'name':procls.name
                }
                list_.append(data)
            return jsonify(list_)
        else:
            return jsonify([])

    def post(self):
        parse = parser.parse_args()
        name = parse.get('name')
        procls = ProCls()
        procls.name = name
        db.session.add(procls)
        db.session.commit()
        return jsonify({'msg':'添加成功！'})


class PutProcls(Resource):
    def put(self,id):
        parse = parser.parse_args()
        name = parse.get('name')
        procls = ProCls.query.filter(ProCls.id==id).first()
        if procls:
            procls.name = name
            db.session.commit()
            data = {
                'id':id,
                'name':name
            }
            return jsonify(data)
        else:
            return jsonify({})


class delProcls(Resource):
    def delete(self,id):
        procls = ProCls.query.filter(ProCls.id==id).first()
        if procls:
            pros = Productions.query.filter(Productions.class_id==procls.id).all()
            if pros:
                for pro in pros:
                    carts = ShopCart.query.filter(ShopCart.pro_id == pro.id).all()
                    if carts:
                        for cart in carts:
                            db.session.delete(cart)
                    else:
                        pass
                    db.session.delete(pro)
            else:
                pass
            db.session.delete(procls)
            db.session.commit()
            return jsonify({'msg':'删除成功！'})
        else:
            return jsonify({})


class GetProcls(Resource):
    def get(self,cls_id):
        list_ = []
        procls = ProCls.query.filter(ProCls.id==cls_id).first()
        pros = Productions.query.filter(Productions.class_id==cls_id).all()
        if pros:
            for pro in pros:
                data = {
                    'cls_id':procls.id,
                    'name':procls.name,
                    'prods':{
                        'id':pro.id,
                        'price':pro.price,
                        'old_price':pro.old_price,
                        'stock':pro.stock,
                        'title':pro.title,
                        'cover_img':pro.cover_img,
                        'content':pro.content,
                    }
                }
                list_.append(data)
            list2 = []
            for i in range(len(list_)):
                if list_[i] != {}:
                    order_list = []
                    order_list.append(list_[i].get('prods'))
                    for j in range(i + 1, len(list_)):
                        if list_[i].get('cls_id') == list_[j].get('cls_id'):
                            order_list.append(list_[j].get('prods'))
                            list_[i]['prods'] = order_list
                            list_[j] = {}

                    list2.append(list_[i])
            for k in list2:
                if isinstance(k['prods'], dict):
                    list_k = []
                    list_k.append(k['prods'])
                    k['prods'] = list_k
            return jsonify(list2)
        else:
            return jsonify({})
