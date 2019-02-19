# 定义资源
from flask_restful import Resource, reqparse
from App.alipay import alipay

parser = reqparse.RequestParser()
parser.add_argument(name='price',type=float)
parser.add_argument(name='d_code',type=str)


class Pay(Resource):
    def post(self):
        parse = parser.parse_args()
        price = parse.get('price')
        d_code = parse.get('d_code')

        url = alipay.direct_pay(
            subject="测试订单",  # 订单名称
            # 订单号生成，一般是当前时间(精确到秒)+用户ID+随机数
            out_trade_no=d_code,  # 订单号
            total_amount=price,  # 支付金额
            return_url="http://192.168.1.100:5000/api/<result>/" # 支付成功后，跳转url 【客户端显示】
        )

        # 将前面后的支付参数，拼接到支付网关
        # 注意：下面支付网关是沙箱环境，最终进行签名后组合成支付宝的url请求
        re_url = "https://openapi.alipay.com/gateway.do?{data}".format(data=url)


        # 返回的是支付宝的支付地址
        return {'re_url': re_url}
