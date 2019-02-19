from flask import jsonify
from flask_restful import reqparse, Resource

from App.models import Orders, db

parser = reqparse.RequestParser()
parser.add_argument(name='app_id',type=str)
parser.add_argument(name='sign',type=str)
parser.add_argument(name='trade_no',type=str)
parser.add_argument(name='out_trade_no',type=str)
parser.add_argument(name='buyer_logon_id',type=str)
parser.add_argument(name='trade_status',type=str)




class YibuResource(Resource):
    def post(self):

        #获取支付宝异步返回参数
        parse = parser.parse_args()
        app_id = parse.get('app_id')
        sign = parse.get('sign')
        trade_no = parse.get('trade_no')
        out_trade_no = parse.get('out_trade_no')
        buyer_logon_id = parse.get('buyer_logon_id')
        trade_status = parse.get('trade_status')

        print(app_id)
        print(sign)
        print(trade_no)
        print(out_trade_no)
        print(buyer_logon_id)
        print(trade_status)



        order = Orders.query.filter(Orders.d_code==out_trade_no).first()
        if order:
            order.status = True
            db.session.commit()
            #支付宝只识别 'success'
            return 'success'
        else:
            return jsonify({'msg':'订单失败！'})

