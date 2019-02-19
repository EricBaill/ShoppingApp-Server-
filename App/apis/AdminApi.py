from flask import jsonify
from flask_restful import reqparse, Resource, fields, marshal_with
from App.models import db, Admin

parser = reqparse.RequestParser()
parser.add_argument(name='name',type=str,required=True,help='用户名字不能为空')
parser.add_argument(name='phone',type=str,required=True,help='手机号不能为空')
parser.add_argument(name='pwd',type=str,required=True,help='密码不能为空')
parser.add_argument(name='is_super',type=int,required=True,help='请设置权限')

users_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'phone': fields.String,
    'pwd': fields.String,
    'is_super': fields.Integer,
    'create_at': fields.DateTime,
    'update_at': fields.DateTime
}

results_fields = {
    'code': fields.String,
    'message': fields.String,
    'admin_users': fields.Nested(users_fields),
}

class AdminResource(Resource):
    @marshal_with(results_fields)
    def get(self):
        super_users = Admin.query.all()
        if super_users:
            return {'code': '200', 'admin_users':super_users}
        else:
            return {'code':'404','message':'暂无用户信息！'}

    @marshal_with(results_fields)
    def post(self):
        parse = parser.parse_args()
        name = parse.get('name')
        phone = parse.get('phone')
        pwd = parse.get('pwd')
        is_super = parse.get('is_super')
        print(is_super)
        admins = Admin.query.filter(Admin.name.__eq__(name)).first()
        if not admins:
            admin = Admin()
            admin.name = name
            admin.phone = phone
            admin.pwd = pwd
            admin.is_super = is_super
            try:
                db.session.add(admin)
                db.session.commit()
            except Exception as e:
                print(str(e))
            return {'code': '200', 'admin_users': admin}
        else:
            return {'message':'用户名已存在！'}

class AdminResource1(Resource):

    @marshal_with(results_fields)
    def put(self,user_id):
        parse = parser.parse_args()
        name = parse.get('name')
        phone = parse.get('phone')
        pwd = parse.get('pwd')
        is_super = parse.get('is_super')
        print(is_super)

        admin = Admin.query.filter(Admin.id.__eq__(user_id)).first()
        if admin:
            admin.name = name
            admin.phone = phone
            admin.pwd = pwd
            admin.is_super = is_super
            db.session.commit()
            return {'code': '200', 'admin_users': admin}
        else:
            return {'code': '404', 'message': '暂无用户信息！'}


    def delete(self,user_id):
        admin = Admin.query.filter(Admin.id.__eq__(user_id)).first()
        if admin:
            db.session.delete(admin)
            db.session.commit()
            return jsonify({'code':'200','message':'删除成功！'})
        else:
            return jsonify({'code': '404', 'message': '暂无用户信息！'})
