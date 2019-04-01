# -*- coding: utf-8 -*-
from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import Address, db

class GetAddress(Resource):
    def get(self,user_id):
        list_ = []
        addresss = Address.query.filter(Address.user_id==user_id,Address.status==0).all()
        if addresss:
            for address in addresss:
                data = {
                    'id':address.id,
                    'receiver':address.linkman,
                    'phone':address.tel,
                    'details':address.detail,
                    'isDefault':address.is_default
                }
                list_.append(data)
            return jsonify(list_)
        else:
            return jsonify([])

class AddAddress(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='user_id', type=int)
        parser.add_argument(name='receiver', type=str)
        parser.add_argument(name='phone', type=str)
        parser.add_argument(name='details', type=str)
        parser.add_argument(name='isDefault', type=int)
        parse = parser.parse_args()
        user_id = parse.get('user_id')
        linkman = parse.get('receiver')
        tel = parse.get('phone')
        detail = parse.get('details')
        is_default = parse.get('isDefault')
        addres = Address.query.all()
        if is_default == 1:
            if addres:
                for addre in addres:
                    if addre.is_default == 1:
                        addre.is_default = 0
                        db.session.commit()
                    else:
                        pass

                address = Address()
                address.user_id = user_id
                address.linkman = linkman
                address.tel = tel
                address.detail = detail
                address.is_default = is_default
                db.session.add(address)
                db.session.commit()
                return jsonify({'msg':'添加成功！'})
            else:
                address = Address()
                address.user_id = user_id
                address.linkman = linkman
                address.tel = tel
                address.detail = detail
                address.is_default = is_default
                db.session.add(address)
                db.session.commit()
                return jsonify({'msg': '添加成功！'})

        elif is_default == 0:
            address = Address()
            address.user_id = user_id
            address.linkman = linkman
            address.tel = tel
            address.detail = detail
            address.is_default = is_default
            db.session.add(address)
            db.session.commit()
            return jsonify({'msg': '添加成功！'})



class PutAddress(Resource):
    def put(self,user_id,add_id):
        parser = reqparse.RequestParser()
        parser.add_argument(name='receiver', type=str)
        parser.add_argument(name='phone', type=str)
        parser.add_argument(name='details', type=str)
        parser.add_argument(name='isDefault', type=int)
        parse = parser.parse_args()
        linkman = parse.get('receiver')
        tel = parse.get('phone')
        detail = parse.get('details')
        is_default = parse.get('isDefault')

        address = Address.query.filter(Address.user_id==user_id,Address.id==add_id).first()
        addres = Address.query.all()
        if address:
            if is_default == 1:
                if addres:
                    for addre in addres:
                        if addre.is_default == 1:
                            addre.is_default = 0
                            db.session.commit()
                        else:
                            pass

                    address.user_id = user_id
                    address.linkman = linkman
                    address.tel = tel
                    address.detail = detail
                    address.is_default = is_default
                    db.session.commit()
                    return jsonify({'msg':'编辑成功！'})
                else:
                    return jsonify({})

            elif is_default == 0:
                address.user_id = user_id
                address.linkman = linkman
                address.tel = tel
                address.detail = detail
                address.is_default = is_default
                db.session.commit()
                return jsonify({'msg': '编辑成功！'})
        else:
            return jsonify({})


class DelAddress(Resource):
    def get(self,user_id,add_id):
        address = Address.query.filter(Address.user_id==user_id,Address.id==add_id).first()
        if address:
            address.status = 1
            db.session.commit()
            return jsonify({'msg':'删除成功！'})
        else:
            return jsonify({})