from flask_restful import Resource


class SucessPayResource(Resource):
    def get(self):
        return '支付成功！'