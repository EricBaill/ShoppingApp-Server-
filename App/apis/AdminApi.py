# -*- coding: utf-8 -*-
from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import Admin, db

parser = reqparse.RequestParser()
parser.add_argument(name='account', type=str)
parser.add_argument(name='pwd', type=str)


class addAdmin(Resource):
    def post(self):
        parse = parser.parse_args()
        account = parse.get('account')
        pwd = parse.get('pwd')
        admin = Admin()
        admin.account = account
        admin.pwd = pwd
        db.session.add(admin)
        db.session.commit()
        return jsonify({'msg':'添加成功'})


class LoginAdmin(Resource):
    def post(self):
        parse = parser.parse_args()
        account = parse.get('account')
        pwd = parse.get('pwd')
        admin = Admin.query.filter(Admin.account==account,Admin.pwd==pwd).first()
        print(admin)
        if admin:
            data = {
                'id':admin.id,
                'account':admin.account,
                'pwd':admin.pwd,
                'is_super':admin.is_super,
                'create_at':admin.create_at
            }
            return jsonify(data)
        else:
            return jsonify('err')


class getAdmin(Resource):
    def get(self):
        list_ = []
        admins = Admin.query.all()
        if admins:
            for admin in admins:
                data = {
                    'id':admin.id,
                    'account':admin.account,
                    'pwd':admin.pwd,
                    'create_at':admin.create_at,
                    'is_super':admin.is_super
                }
                list_.append(data)
            return jsonify(list_)
        else:
            return jsonify([])


class putAdmin(Resource):
    def put(self,id):
        admin = Admin.query.filter(Admin.id==id).first()
        parse = parser.parse_args()
        account = parse.get('account')
        pwd = parse.get('pwd')
        if admin:
            admin.account = account
            admin.pwd = pwd
            db.session.commit()
            return jsonify({'msg':'成功'})
        else:
            return jsonify({})


class delAdmin(Resource):
    def delete(self,id):
        admin = Admin.query.filter(Admin.id==id).first()
        if admin:
            db.session.delete(admin)
            db.session.commit()
            return jsonify({'msg':'成功'})
        else:
            return jsonify({})


class setManager(Resource):
    def get(self,id):
        admin  = Admin.query.filter(Admin.id==id).first()
        if admin:
            if admin.is_super == 0:
                admin.is_super = 1
            elif admin.is_super == 1:
                admin.is_super = 0
            else:
                pass
            db.session.commit()
            return jsonify({'msg': '成功'})
        else:
            return jsonify({})