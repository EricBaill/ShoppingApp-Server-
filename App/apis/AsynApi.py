# -*- coding: utf-8 -*-

from flask_restful import Resource

from App.models import Orders, db


class Asyn(Resource):
    def post(self):
        orders = Orders.query.all()
        if orders:
            orders[-1].status = 1
            db.session.commit()
        else:
            pass

        return 'success'