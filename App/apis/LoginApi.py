from flask_restful import Resource, reqparse, marshal_with, fields
from App.models import User

parser = reqparse.RequestParser()
parser.add_argument(name='phone',type=str,required=True,help='请填写手机号')
parser.add_argument(name='pwd',type=str,required=True,help='请填写密码')

user_fields = {
    'id':fields.Integer,
    'name':fields.String,
    'phone':fields.String,
}

result_fields = {
    'code':fields.String,
    'message': fields.String,
    'data':fields.Nested(user_fields),
}

class LoginResource(Resource):
    @marshal_with(result_fields)
    def post(self):
        parse = parser.parse_args()
        phone = parse.get('phone')
        pwd = parse.get('pwd')
        users = User.query.filter(User.phone.__eq__(phone)).first()
        if users:
            if users.pwd == pwd:
                return {'code':'200','data':users}
            else:
                return {'code':'401','message':'您输入的密码有误，请重新输入！'}
        else:
            return {'code':'401','message':'用户不存在！'}

