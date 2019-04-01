from flask import jsonify
from flask_restful import reqparse, Resource
from App.models import Productions, db, ProCls

parser = reqparse.RequestParser()


class Productin_(Resource):
    def get(self):
        pro_classes = ProCls.query.filter(ProCls.id == Productions.class_id).all()
        productions = Productions.query.filter(Productions.class_id == ProCls.id).all()
        list_ = []
        for pro_class in pro_classes:
            for production in productions:
                if production.class_id == pro_class.id:
                    data = {
                        'class_id':pro_class.id,
                        'class_name':pro_class.name,
                        'foods':{
                            'id':production.id,
                            'name':production.name,
                            'price':production.price,
                            'old_price':production.old_price,
                            'stock':production.stock,
                            'title':production.title,
                            'cover_img':production.cover_img,
                            'content':production.content,
                            'class_id':production.class_id,
                        }
                    }
                    list_.append(data)
        list2 = []
        for i in range(len(list_)):
            if list_[i] != {}:
                order_list = []
                order_list.append(list_[i].get('foods'))
                for j in range(i+1,len(list_)):
                    if list_[i].get('class_id') == list_[j].get('class_id'):
                        order_list.append(list_[j].get('foods'))
                        list_[i]['foods'] = order_list
                        list_[j] = {}

                list2.append(list_[i])
        for k in list2:
            if isinstance(k['foods'], dict):
                list_k = []
                list_k.append(k['foods'])
                k['foods'] = list_k
        return jsonify(list2)

    def post(self):
        parser.add_argument(name='name', type=str, required=True, help='商品名不能为空')
        parser.add_argument(name='price', type=float)
        parser.add_argument(name='old_price', type=float)
        parser.add_argument(name='stock', type=str)
        parser.add_argument(name='title', type=str)
        parser.add_argument(name='cover_img', type=str)
        parser.add_argument(name='content', type=str)
        parser.add_argument(name='class_id', type=int)
        parse = parser.parse_args()
        name = parse.get('name')
        price = parse.get('price')
        old_price = parse.get('price')
        stock = parse.get('stock')
        title = parse.get('title')
        cover_img = parse.get('cover_img')
        content = parse.get('content')
        class_id = parse.get('class_id')

        pro = Productions()
        pro.name = name
        pro.price = price
        pro.old_price = old_price
        pro.stock = stock
        pro.title = title
        pro.cover_img = cover_img
        pro.content = content
        pro.class_id = class_id
        try:
            db.session.add(pro)
            db.session.commit()
        except Exception as e:
            print(str(e))

        pro_class = ProCls.query.filter(ProCls.id.__eq__(class_id)).first()


class Productin_1(Resource):
    def get(self):
        list_ = []
        productions = Productions.query.filter(Productions.commend==1).all()
        if productions:
            for production in productions:
                data = {
                    'id': production.id,
                    'name': production.name,
                    'price': production.price,
                    'stock': production.stock,
                    'title': production.title,
                    'cover_img': production.cover_img,
                }
                list_.append(data)
            return jsonify(list_)
        else:
            return jsonify([])


class PutProductin(Resource):
    def put(self,id):
        parser.add_argument(name='class_name', type=str)
        parser.add_argument(name='name', type=str)
        parser.add_argument(name='price', type=float)
        parser.add_argument(name='old_price', type=float)
        parser.add_argument(name='stock', type=str)
        parser.add_argument(name='title', type=str)
        parser.add_argument(name='cover_img', type=str)
        parser.add_argument(name='content', type=str)
        parser.add_argument(name='class_id', type=int)
        parse = parser.parse_args()
        name = parse.get('name')
        price = parse.get('price')
        old_price = parse.get('price')
        stock = parse.get('stock')
        title = parse.get('title')
        cover_img = parse.get('cover_img')
        content = parse.get('content')
        class_id = parse.get('class_id')
        productions = Productions.query.filter(Productions.id==id).first()
        if productions:
            pro = Productions()
            pro.name = name
            pro.price = price
            pro.old_price = old_price
            pro.stock = stock
            pro.title = title
            pro.cover_img = cover_img
            pro.content = content
            pro.class_id = class_id
            try:
                db.session.add(pro)
                db.session.commit()
            except Exception as e:
                print(str(e))


class ProInfos(Resource):
    def get(self,id):
        list_ = []
        production = Productions.query.filter(Productions.id == id).first()
        pro_class = ProCls.query.filter(ProCls.id == production.class_id).first()
        if production.class_id == pro_class.id:
            pros = Productions.query.filter(Productions.class_id==production.class_id).all()
            if pros:
                for pro in pros:
                    data = {
                        'class_id': production.class_id,
                        'id': production.id,
                        'name': production.name,
                        'price': production.price,
                        'old_price': production.old_price,
                        'stock': production.stock,
                        'title': production.title,
                        'cover_img': production.cover_img,
                        'content': production.content,
                        'sameProducts':{
                            'id': pro.id,
                            'name': pro.name,
                            'price': pro.price,
                            'old_price': pro.old_price,
                            'stock': pro.stock,
                            'title': pro.title,
                            'cover_img': pro.cover_img,
                            'content': pro.content,
                        }
                    }
                    list_.append(data)
                list2 = []
                for i in range(len(list_)):
                    if list_[i] != {}:
                        order_list = []
                        order_list.append(list_[i].get('sameProducts'))
                        for j in range(i + 1, len(list_)):
                            if list_[i].get('class_id') == list_[j].get('class_id'):
                                order_list.append(list_[j].get('sameProducts'))
                                list_[i]['sameProducts'] = order_list
                                list_[j] = {}

                        list2.append(list_[i])
                for k in list2:
                    if isinstance(k['sameProducts'], dict):
                        list_k = []
                        list_k.append(k['sameProducts'])
                        k['sameProducts'] = list_k
                return jsonify(list2)
        else:
            return jsonify({})

class DelProductin(Resource):
    def delete(self,id):
        pro = Productions.query.filter(Productions.id==id).first()
        if pro:
            db.session.delete(pro)
            db .session.commit()
            return jsonify({'msg':'删除成功'})
        else:
            return jsonify({})