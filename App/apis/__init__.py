# -*- coding: utf-8 -*-

from flask_restful import Api

from App.apis.AProductsApi import AdminPro, AdminPro1, AdminPro2
from App.apis.AddressApi import AddrResource, AddrResource1
from App.apis.AdminApi import AdminResource, AdminResource1
from App.apis.AdminLoginApi import AdminLogin
from App.apis.AlipayApi import Pay
from App.apis.CancelOrderApi import CancelOrder
from App.apis.CommendApi import CommendResource, CommendResource1
from App.apis.LoginApi import LoginResource
from App.apis.OrdersApi import OrderResource, OrderResource1, OrderResource2, OrderResource3, OrderResource4, \
    OrderResource5
from App.apis.ProDetailsApi import ProDetails, ProDetails1, ProDetails3, ProDetails2
from App.apis.Product_classesApi import Pro_classesResource, Pro_classesResource1
from App.apis.ProductionsApi import ProductinsResource, ProductinsResource1
from App.apis.ReceivedApi import Received
from App.apis.RegisterApi import RegisterResource
from App.apis.ResultApi import Result
from App.apis.SaveOrderApi import SaveOrder
from App.apis.SearchProductApi import SearchProductResource
from App.apis.SucessPayApi import SucessPayResource
from App.apis.UploadFileApi import Upload
from App.apis.UserApi import UserResource, UserResource1
from App.apis.YibuApi import YibuResource
from App.apis.shopCartApi import ShopCartResource

api = Api()
#需要注意  api的初始化 要和init方法联系 否则无法初始化
def init_apis(app):
    api.init_app(app=app)

#用户注册
api.add_resource(RegisterResource,'/api/users/')
#用户登录
api.add_resource(LoginResource,'/api/user_login/')

#地址
#用户地址查询
api.add_resource(AddrResource,'/api/address/<int:user_id>/')
#用户地址添加
api.add_resource(AddrResource1,'/api/address/')

#商品
#查询和添加商品
api.add_resource(ProductinsResource,'/api/productions/')

#管理端
api.add_resource(AdminPro,'/api/admin/productions/')
api.add_resource(AdminPro1,'/api/admin/productions/<id>/')
api.add_resource(AdminPro2,'/api/admin/productions/shelf/')

api.add_resource(ProDetails,'/api/productions/details/')
api.add_resource(ProDetails1,'/api/productions/details/<user_id>/')
api.add_resource(ProDetails2,'/api/production/add/<pro_id>/user/<user_id>/')
api.add_resource(ProDetails3,'/api/production/delete/<pro_id>/user/<user_id>/')
#修改商品信息
api.add_resource(ProductinsResource1,'/api/productions/<int:production_id>/')
#搜索商品
api.add_resource(SearchProductResource,'/api/search/')

#管理员
#查询和添加管理员信息
api.add_resource(AdminResource,'/api/admin_users/')

api.add_resource(AdminLogin,'/api/admin/login/')


#修改、删除管理员信息
api.add_resource(AdminResource1,'/api/admin_users/<int:user_id>/')

#获取和添加商品类别
api.add_resource(Pro_classesResource,'/api/product_classes/')
api.add_resource(Pro_classesResource1,'/api/product_classes/delete/<id>/')

#订单
#获取用户订单信息
api.add_resource(OrderResource,'/api/order/<int:user_id>/')
#修改订单
api.add_resource(OrderResource1,'/api/orders/<int:order_id>/')
api.add_resource(OrderResource2,'/api/orders/status/')

api.add_resource(OrderResource3,'/api/orders/list/')
api.add_resource(OrderResource4,'/api/orders/month/list/')
#添加订单
# api.add_resource(OrderResource5,'/api/order/')

#查询和添加购物车
api.add_resource(ShopCartResource,'/api/cart/')

#支付宝支付
api.add_resource(SucessPayResource,'/api/sucesspay/')
api.add_resource(Pay,'/api/pay/')
api.add_resource(SaveOrder,'/api/save/order/')
api.add_resource(CancelOrder,'/api/cancel/order/<id>/')

api.add_resource(Received,'/api/isreceived/<id>/')



api.add_resource(YibuResource,'/api/yibu/')
api.add_resource(Result,'/api/<result>/')



api.add_resource(UserResource,'/api/user/info/')
api.add_resource(UserResource1,'/api/user/address/<id>/')
api.add_resource(OrderResource5,'/api/order/send/')

#推荐商品
api.add_resource(CommendResource,'/api/iscommend/')
api.add_resource(CommendResource1,'/api/iscommend/<id>/')


api.add_resource(Upload,'/api/upload/old/')


