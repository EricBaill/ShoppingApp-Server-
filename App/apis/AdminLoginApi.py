from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import Admin


class AdminLogin(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='name', type=str)
        parser.add_argument(name='pwd', type=str)
        parse = parser.parse_args()
        name = parse.get('name')
        pwd = parse.get('pwd')
        admin = Admin.query.filter(Admin.name.__eq__(name)).first()
        if admin:
            if admin.pwd == pwd:
                data = {
                    'id':admin.id,
                    'name':name,
                    'is_super':admin.is_super
                }
                return jsonify(data)
            else:
                return jsonify({'msg':'密码有误！'})
        else:
            return jsonify({'msg':'用户不存在！'})