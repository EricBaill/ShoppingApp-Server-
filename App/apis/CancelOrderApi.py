# -*- coding: utf-8 -*-

from flask import jsonify
from flask_restful import Resource

from App.models import Orders, db


class CancelOrder(Resource):
    def delete(self,id):
        order = Orders.query.filter(Orders.id==id).first()
        if order:
            db.session.delete(order)
            db.session.commit()
            return jsonify({'msg':'订单取消成功！'})
        else:
            return jsonify({'msg':'暂无订单信息！'})