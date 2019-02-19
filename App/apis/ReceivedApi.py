# -*- coding: utf-8 -*-
from flask import jsonify
from flask_restful import Resource

from App.models import Orders, db


class Received(Resource):
    def get(self,id):
        order = Orders.query.filter(Orders.id==id).first()
        if order:
            order.is_receive = 1
            db.session.commit()
            return jsonify({'msg':'订单已签收！'})
        else:
            return jsonify({'msg':'暂无订单信息！'})