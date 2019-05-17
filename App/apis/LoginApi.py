from flask import jsonify
from flask_restful import Resource, reqparse
from App.models import User, db

parser = reqparse.RequestParser()
parser.add_argument(name='phone',type=str)


class Login(Resource):
    def post(self):
        parse = parser.parse_args()
        phone = parse.get('phone')
        u = User.query.filter(User.phone==phone).first()
        if u:
            data = {
                'id': u.id,
                'phone': u.phone
            }
            return jsonify(data)

        else:
            user = User()
            user.phone = phone
            db.session.add(user)
            db.session.commit()
            u = User.query.filter(User.phone==phone).first()
            data = {
                'id': u.id,
                'phone': phone
            }
            return jsonify(data)


class confirmLogin(Resource):
    def post(self):
        parse = parser.parse_args()
        phone = parse.get('phone')
        user = User.query.filter(User.phone == phone).first()
        if user:
            data = {
                'msg': 1
            }
            return jsonify(data)
        else:
            data = {
                'msg': 0
            }
            return jsonify(data)
