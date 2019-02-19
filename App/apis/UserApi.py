from flask import jsonify
from flask_restful import Resource

from App.models import User, Desc


class UserResource(Resource):
    def get(self):
        users = User.query.all()
        list_ = []
        if users:
            for user in users:
                data = {
                    'id':user.id,
                    'name':user.name,
                    'phone':user.phone,
                    'pwd':user.pwd,
                }
                list_.append(data)
            return  jsonify(list_)
        else:
            return jsonify([])

class UserResource1(Resource):
    def get(self,id):
        list_ = []
        address = Desc.query.filter(Desc.user_id.__eq__(id)).all()
        if address:
            for add in address:
                data = {
                    'id':add.id,
                    'province':add.province,
                    'city':add.city,
                    'area':add.area,
                    'detail':add.detail,
                    'is_default':add.is_default,
                    'name':add.linkman,
                    'phone':add.link_phone
                }
                list_.append(data)
            return jsonify(list_)
        else:
            return jsonify([])