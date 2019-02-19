# -*- coding: utf-8 -*-
from flask import jsonify

from flask_restful import Resource


class Result(Resource):
    def get(self,result):


        print(result)

        return jsonify(result)

'''
charset=utf-8&out_trade_no=1547623746781&method=alipay.trade.wap.pay.return&total_amount=0.01&sign=dCiTep7wWMpCzZX1tHSCjmG0X7znbNtisgC8DOekR7H2I5CY7NGjHWobH%2BOK6WhnYRrm7qnkwEWtPZuXS9iEFN2ui7hmz5bGnWFwnXujVceqKHWqxWDb0R32nXvV%2F3bUx5BJPkAUP5wJYqH%2BZ3adBfSnodANS%2Fl1La6h0pgyzqnAZOuQYtdcffEGjQFkomkd7txaKwT9JBwKQ5jpBdgY93o4B4Y6I2FN0DnE0x5KUqQ6y3Qo%2B2w6ZMY5MQMJ1uLPC03RYZz6w5crmuJPURYjbFSuKm5NIZBPw1%2BwGky3ROQMyAv9E4hD53Nw98356HJtQFGj272hjM%2Fh%2Fv4cK2yuBQ%3D%3D&trade_no=2019011622001494281012047350&auth_app_id=2018112062214560&version=1.0&app_id=2018112062214560&sign_type=RSA2&seller_id=2088331509978030&timestamp=2019-01-16+15%3A29%3A14 
'''