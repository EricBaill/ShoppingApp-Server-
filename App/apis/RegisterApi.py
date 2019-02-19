from flask_restful import reqparse, Resource, fields, marshal_with
from App.models import db, User

parser = reqparse.RequestParser()
parser.add_argument(name='name',type=str,required=True,help='用户名字不能为空')
parser.add_argument(name='phone',type=str,required=True,help='手机号不能为空')
parser.add_argument(name='pwd',type=str,required=True,help='密码不能为空')

class RegisterResource(Resource):
    users_fields={
        'id':fields.Integer,
        'name':fields.String,
        'phone':fields.String,
        'pwd':fields.String,
        'create_at':fields.DateTime,
        'update_at':fields.DateTime,
    }

    results_fields={
        'code':fields.String,
        'data':fields.Nested(users_fields),
    }

    @marshal_with(results_fields)
    def get(self):
        users = User.query.all()
        return {'code': '200', 'data': users}




    user_fields={
        'id': fields.Integer,
        'name':fields.String,
        'phone':fields.String,
        'pwd':fields.String,
        'create_at': fields.DateTime,
    }

    result_fields={
        'code':fields.String,
        'message': fields.String,
        'data':fields.Nested(user_fields),
    }

    @marshal_with(result_fields)
    def post(self):
        parse = parser.parse_args()
        name = parse.get('name')
        phone = parse.get('phone')
        pwd = parse.get('pwd')
        user = User()
        user.name = name
        user.phone = phone
        user.pwd = pwd
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            print(str(e))
            return {'code':'412','message':'用户名或手机号已存在，请核实后再注册！'}
        return {'code': '200', 'data': user}