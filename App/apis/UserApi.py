from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import User, db


class GetUser(Resource):
    def get(self):
        users = User.query.all()
        list_ = []
        if users:
            for user in users:
                data = {
                    'id': user.id,
                    'name': user.name,
                    'phone': user.phone,
                }
                list_.append(data)
            return jsonify(list_)
        else:
            return jsonify([])


class PutUser(Resource):
    def put(self,id):
        parser = reqparse.RequestParser()
        parser.add_argument(name='name', type=str)
        parser.add_argument(name='phone', type=str)
        parse = parser.parse_args()
        name = parse.get('name')
        phone = parse.get('phone')
        user = User.query.filter(User.id==id).first()
        if user:
            user.name = name
            user.phone = phone
            db.session.commit()
            data = {
                'id': user.id,
                'name': name,
                'phone': phone
            }
            return jsonify(data)
        else:
            return jsonify({})

class delUser(Resource):
    def delete(self ,id):
        user = User.query.filter(User.id==id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({'msg': '删除成功！'})
        else:
            return jsonify({})



# class User_1(Resource):
#     def get(self,id):
#         list_ = []
#         address = Order_user.query.filter(Order_user.user_id.__eq__(id)).all()
#         if address:
#             for add in address:
#                 data = {
#                     'id':add.id,
#                     'province':add.d_province,
#                     'city':add.d_city,
#                     'area':add.d_area,
#                     'detail':add.d_detail,
#                     'is_default':add.is_default,
#                     'name':add.d_linkman,
#                     'phone':add.d_link_phone
#                 }
#                 list_.append(data)
#             return jsonify(list_)
#         else:
#             return jsonify([])