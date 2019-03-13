from flask import jsonify
from flask_restful import Resource, reqparse
from App.models import User, db

parser = reqparse.RequestParser()
parser.add_argument(name='phone',type=str,required=True,help='请填写手机号')


class Login(Resource):
    def post(self):
        parse = parser.parse_args()
        phone = parse.get('phone')
        u = User.query.filter(User.phone==phone).first()
        if u:
            return jsonify({'msg':'登录成功！'})
        else:
            user = User()
            user.phone = phone
            user.head_img = 'http://soft1906.xin/head_img.jpeg'
            db.session.add(user)
            db.session.commit()
            return jsonify({'msg':'登录成功！'})
