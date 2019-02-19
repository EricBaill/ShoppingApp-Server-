from flask import jsonify
from flask_restful import reqparse, Resource, fields, marshal_with
from App.models import User, db, Desc

parser = reqparse.RequestParser()
parser.add_argument(name='id',type=int,required=True,help='用户id不能为空')
parser.add_argument(name='name',type=str,required=True,help='用户名不能为空')
parser.add_argument(name='province',type=str,required=True,help='省份不能为空')
parser.add_argument(name='city',type=str,required=True,help='城市不能为空')
parser.add_argument(name='area',type=str,required=True,help='地区不能为空')
parser.add_argument(name='linkman',type=str,required=True,help='联系人不能为空')
parser.add_argument(name='link_phone',type=str,required=True,help='联系人手机号不能为空')
parser.add_argument(name='is_default',type=bool)
parser.add_argument(name='detail',type=str)

desc_fields = {
    'id': fields.Integer,
    'province': fields.String,
    'city': fields.String,
    'area': fields.String,
    'detail': fields.String,
    'is_default': fields.Boolean,
    'linkman': fields.String,
    'link_phone': fields.String,
}

user_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'phone': fields.String,
}

users_fields = {
    'create_at': fields.DateTime,
    'update_at': fields.DateTime,
}

results_fields = {
    'code': fields.String,
    'message': fields.String,
    'address': fields.Nested(user_fields),
    'desc': fields.Nested(desc_fields),
    'date': fields.Nested(users_fields),
}

class AddrResource(Resource):
    @marshal_with(results_fields)
    def get(self,user_id):
        user = User.query.filter(User.id.__eq__(user_id)).all()
        desc = Desc.query.filter(Desc.user_id.__eq__(user_id)).all()
        if user:
            return {'code': '200', 'address': user,'desc':desc,'date': user}
        else:
            return {'code': '404', 'message': '暂无任何信息！'}


class AddrResource1(Resource):
    def post(self):
        parse = parser.parse_args()
        id = parse.get('id')
        province = parse.get('province')
        city = parse.get('city')
        area = parse.get('area')
        detail = parse.get('detail')
        linkman = parse.get('linkman')
        link_phone = parse.get('link_phone')
        is_default = parse.get('is_default')
        desc = Desc()
        desc.province = province
        desc.city = city
        desc.area = area
        desc.detail = detail
        desc.linkman = linkman
        desc.link_phone = link_phone
        desc.user_id = id
        desc.is_default = is_default
        try:
            db.session.add(desc)
            db.session.commit()
        except Exception as e:
            print(str(e))
        return jsonify({'msg':'ok','code':'200'})