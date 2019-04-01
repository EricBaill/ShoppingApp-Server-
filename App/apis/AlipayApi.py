# 定义资源
from flask_restful import Resource, reqparse
from App.alipay import alipay
from App.models import Orders


class Pay(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='order_id', type=int)
        parse = parser.parse_args()
        order_id = parse.get('order_id')
        order=  Orders.query.filter(Orders.id==order_id).first()

        # 获取订单号，根据订单生成 支付订单
        # 支付订单包括: 订单号、支付金额、订单名称
        # 传递参数执行支付类里的direct_pay方法，返回签名后的支付参数，
        url = alipay.direct_pay(
            subject="测试订单	",  # 订单名称
            # 订单号生成，一般是当前时间(精确到秒)+用户ID+随机数
            out_trade_no=order.code,  # 订单号
            total_amount=order.sumprice,  # 支付金额
            return_url="http://www.jxtidea.com"  # 支付成功后，跳转url 【客户端显示】
        )

        # 将前面后的支付参数，拼接到支付网关
        # 注意：下面支付网关是沙箱环境，最终进行签名后组合成支付宝的url请求
        re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)

        print(re_url)

        # 返回的是支付宝的支付地址
        return {'re_url': re_url}
