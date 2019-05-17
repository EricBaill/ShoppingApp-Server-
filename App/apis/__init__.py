from flask_restful import Api

from App.apis.AddressApi import AddAddress, PutAddress, GetAddress, DelAddress
from App.apis.AdminApi import addAdmin, getAdmin, setManager, putAdmin, delAdmin, LoginAdmin
from App.apis.AlipayApi import Pay
from App.apis.AsynApi import Asyn
from App.apis.CarouselApi import getCarousel, getCarousel_, getAllCarousels, addCarousel, putCarousel, delCarousel
from App.apis.ConfirmApi import Confirm
from App.apis.LoginApi import Login, confirmLogin
from App.apis.OrderApi import GetOrder_, DelOrder_, addOrder_, GetOrder_01, DelOrder_01, getOrders_, isSend, \
    searchTelOrder
from App.apis.ProClsApi import ProductionCls, GetProcls, delProcls, PutProcls
from App.apis.ProductionApi import Productin_, PutProductin, ProInfos, DelProductin, Productin_1, getPros, proCommend
from App.apis.ShopCartApi import ShopCart_, GetShopCart, DelShopCart, AddShopCart, CutShopCart
from App.apis.UserApi import GetUser, delUser

api = Api()
#需要注意  api的初始化 要和init方法联系 否则无法初始化
def init_apis(app):
    api.init_app(app=app)


#添加管理员
api.add_resource(addAdmin,'/api/add/admin/')
#获取管理员
api.add_resource(getAdmin,'/api/get/all/admins/')
#设置超级管理员
api.add_resource(setManager,'/api/set/admin/manager/<id>/')
#修改管理员信息
api.add_resource(putAdmin,'/api/put/admin/<id>/')
#删除管理员
api.add_resource(delAdmin,'/api/del/admin/<id>/')
#管理员登录
api.add_resource(LoginAdmin,'/api/admin/login/')


#用户登录
api.add_resource(Login,'/api/user/login/')
#用户登录验证
api.add_resource(confirmLogin,'/api/user/login/confirm/')
#获取用户信息
api.add_resource(GetUser,'/api/user/infos/')
#删除用户信息
api.add_resource(delUser,'/api/delete/user/<id>/')


#获取，添加商品分类
api.add_resource(ProductionCls,'/api/add/get/procls/')
#编辑商品分类
api.add_resource(PutProcls,'/api/put/procls/<id>/')
#删除商品分类
api.add_resource(delProcls,'/api/delete/procls/<id>/')
#获取某一分类下的所有商品信息
api.add_resource(GetProcls,'/api/get/class/pros/<cls_id>/')


#获取，添加商品列表
api.add_resource(Productin_,'/api/productions/')
#管理端获取商品
api.add_resource(getPros,'/api/get/all/productions/')
#显示推荐商品
api.add_resource(Productin_1,'/api/commend/productions/')
#获取商品详情
api.add_resource(ProInfos,'/api/production/info/<id>/')
#修改商品
api.add_resource(PutProductin,'/api/put/production/<id>/')
#删除商品
api.add_resource(DelProductin,'/api/del/production/<id>/')
#设置商品是否推荐
api.add_resource(proCommend,'/api/set/production/commend/<id>/')


#购物车添加
api.add_resource(ShopCart_,'/api/add/shop/cart/')
#获取购物车信息
api.add_resource(GetShopCart,'/api/get/shop/carts/<user_id>/')
#删除购物车
api.add_resource(DelShopCart,'/api/del/shop/<user_id>/cart/<id>/')
#计算添加购物车商品数量
api.add_resource(AddShopCart,'/api/add/number/shopcart/')
#计算减少购物车商品数量
api.add_resource(CutShopCart,'/api/cut/number/shopcart/')


#添加地址
api.add_resource(AddAddress,'/api/add/address/')
#获取用户地址
api.add_resource(GetAddress,'/api/get/address/<user_id>/')
#用户编辑地址
api.add_resource(PutAddress,'/api/put/address/<add_id>/user/<user_id>/')
#用户删除地址
api.add_resource(DelAddress,'/api/del/address/<add_id>/user/<user_id>/')


#提交订单进行支付
api.add_resource(Pay,'/api/alipay/')
#获取订单信息
api.add_resource(GetOrder_,'/api/get/orders/<user_id>/')
#获取订单详情
api.add_resource(GetOrder_01,'/api/get/orders/infos/<order_id>/')
#取消订单
api.add_resource(DelOrder_,'/api/cancel/order/<id>/')
#删除订单
api.add_resource(DelOrder_01,'/api/delete/order/<order_id>/')
#添加订单
api.add_resource(addOrder_,'/api/add/order/')
#管理端获取所有订单
api.add_resource(getOrders_,'/api/get/add/orders/')
#根据地址中联系人手机搜索订单信息
api.add_resource(searchTelOrder,'/api/search/phone/orders/')
#发货
api.add_resource(isSend,'/api/order/send/<id>/')

#收货确认
api.add_resource(Confirm,'/api/confirm/receipt/<order_id>/')

#获取轮播
api.add_resource(getCarousel,'/api/get/carousels/')
#获取轮播详情
api.add_resource(getCarousel_,'/api/get/carousel/info/<id>/')
#获取轮播列表
api.add_resource(getAllCarousels,'/api/get/all/carousels/')
#添加轮播
api.add_resource(addCarousel,'/api/add/carousels/')
#编辑轮播
api.add_resource(putCarousel,'/api/put/carousel/<id>/')
#删除轮播
api.add_resource(delCarousel,'/api/del/carousel/<id>/')

#支付宝异步回调
# api.add_resource(Asyn,'/api/asynchronous/')
api.add_resource(Asyn,'/api/yibu/')
