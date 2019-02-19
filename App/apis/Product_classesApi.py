from flask import jsonify
from flask_restful import reqparse, Resource, fields, marshal_with
from App.models import ProductClass, db

parser = reqparse.RequestParser()
parser.add_argument(name='class_name',type=str,required=True,help='商品类名不能为空')


class Pro_classesResource(Resource):
    pros_classes_fields = {
        'id': fields.Integer,
        'class_name': fields.String,
        'create_at': fields.DateTime,
        'update_at': fields.DateTime
    }

    results_fields = {
        'code': fields.String,
        'message': fields.String,
        'classes': fields.Nested(pros_classes_fields),
    }

    @marshal_with(results_fields)
    def get(self):
        pro_classes = ProductClass.query.all()
        return {'code': '200', 'classes': pro_classes}

    pro_classes_fields = {
        'id': fields.Integer,
        'class_name': fields.String,
    }

    results_field = {
        'code': fields.String,
        'message': fields.String,
        'classes': fields.Nested(pro_classes_fields),
    }

    @marshal_with(results_field)
    def post(self):
        parse = parser.parse_args()
        class_name = parse.get('class_name')
        pro_classes = ProductClass()
        pro_classes.class_name = class_name
        try:
            db.session.add(pro_classes)
            db.session.commit()
        except Exception as e:
            print(str(e))
            return {'code': '403', 'message': '您添加的商品类别有误！'}
        return {'code': '200', 'classes': pro_classes}

class Pro_classesResource1(Resource):

    def delete(self,id):
        pro_cls = ProductClass.query.filter(ProductClass.id.__eq__(id)).first()
        if pro_cls:
            db.session.delete(pro_cls)
            db.session.commit()
            return jsonify({'msg':'删除成功！'})
        else:
            return jsonify({'msg':'暂无信息！'})
