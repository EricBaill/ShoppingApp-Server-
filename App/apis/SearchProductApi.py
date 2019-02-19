from flask_restful import reqparse, Resource, fields, marshal_with
from App.models import Productions

parser = reqparse.RequestParser()
parser.add_argument(name='p_name',type=str,required=True,help='商品名不能为空')

pro_fields = {
    'id': fields.Integer,
    'p_name': fields.String,
    'price': fields.Float,
    'old_price': fields.Float,
    'description': fields.String,
    'amount': fields.String,
    'text1': fields.String,
    'text2': fields.String,
    'img': fields.String,
    'icon': fields.String,
    'info': fields.String,
    'unit': fields.String,
    'sales': fields.String,
    'origin': fields.String,
    'class_id': fields.Integer,
    'create_at': fields.DateTime,
}

pro_class_fields = {
    'class_name': fields.String,
    'id':fields.Integer,
    # 'foods': fields.List(fields.Nested(pro_fields)),
}


results_fields = {
    'code': fields.String,
    'message': fields.String,
    'goods': fields.List(fields.Nested(pro_fields)),
}

class SearchProductResource(Resource):
    @marshal_with(results_fields)
    def post(self):
        parse = parser.parse_args()
        p_name = parse.get('p_name')
        productions = Productions.query.filter(Productions.p_name.like('%'+p_name+'%')).all()
        if productions:
            return {'code': '200', 'goods': productions}
        else:
            return {'code': '404', 'message': '暂无商品信息！'}