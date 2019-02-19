from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import Productions, db


class CommendResource(Resource):
    def get(self):
        list_ = []
        pros = Productions.query.all()
        if pros:
            for pro in pros:
                if pro.commend == 1:
                    data = {
                        'id':pro.id,
                        'p_name':pro.p_name,
                        'price':pro.price,
                        'icon':pro.icon,
                        'old_price':pro.old_price
                    }
                    list_.append(data)
                # else:
                #     return jsonify([])
            return jsonify(list_)

        else:
            return jsonify([])


class CommendResource1(Resource):
    def post(self,id):
        parser = reqparse.RequestParser()
        parser.add_argument(name='commend', type=int)
        parse = parser.parse_args()
        commend = parse.get('commend')

        pro = Productions.query.filter(Productions.id==id).first()
        if pro:
            pro.commend = commend
            db.session.commit()
            return jsonify({'msg':'修改成功！'})
        else:
            return jsonify({'msg':'暂无信息！'})
