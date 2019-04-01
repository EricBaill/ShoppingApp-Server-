# -*- coding: utf-8 -*-
from flask import jsonify
from flask_restful import Resource

from App.models import Orders, db


class Confirm(Resource):
    def get(self,order_id):
        order = Orders.query.filter(Orders.id==order_id).first()
        if order:
            order.status = 3
            db.session.commit()
            return jsonify({'msg':'成功'})
        else:
            return jsonify({})
