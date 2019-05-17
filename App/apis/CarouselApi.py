# -*- coding: utf-8 -*-
from flask import jsonify
from flask_restful import Resource, reqparse

from App.models import Carousel, db


class getCarousel(Resource):
    def get(self):
        list_ = []
        carousels = Carousel.query.order_by(db.desc(Carousel.id)).all()
        if len(carousels) == 1:
            data = {
                'id':carousels[0].id,
                'cover_img':carousels[0].cover_img,
                'content':carousels[0].cover_img
            }
            list_.append(data)
            return jsonify(list_)
        elif len(carousels) == 2:
            for carousel in carousels:
                data = {
                    'id':carousel.id,
                    'cover_img':carousel.cover_img,
                    'content':carousel.content
                }
                list_.append(data)
            return jsonify(list_)
        elif len(carousels) >= 3:
            data = [{
                'id': carousels[0].id,
                'cover_img': carousels[0].cover_img,
                'content': carousels[0].cover_img
            },
            {
                'id': carousels[1].id,
                'cover_img': carousels[1].cover_img,
                'content': carousels[1].cover_img
            },
            {
                'id': carousels[2].id,
                'cover_img': carousels[2].cover_img,
                'content': carousels[2].cover_img
            }
            ]
            return jsonify(data)
        else:
            return jsonify([])


class getCarousel_(Resource):
    def get(self,id):
        car = Carousel.query.filter(Carousel.id==id).first()
        if car:
            data = {
                'id':car.id,
                'cover_img':car.cover_img,
                'content':car.content
            }
            return jsonify(data)
        else:
            return jsonify({})


class getAllCarousels(Resource):
    def get(self):
        cars = Carousel.query.all()
        list_ = []
        if cars:
            for car in cars:
                data = {
                    'id':car.id,
                    'cover_img':car.cover_img,
                    'content':car.content
                }
                list_.append(data)
            return jsonify(list_)
        else:
            return jsonify([])


parser = reqparse.RequestParser()
parser.add_argument(name='cover_img', type=str)
parser.add_argument(name='content', type=str)


class addCarousel(Resource):
    def post(self):
        parse = parser.parse_args()
        cover_img = parse.get('cover_img')
        content = parse.get('content')
        car = Carousel()
        car.cover_img = cover_img
        car.content = content
        db.session.add(car)
        db.session.commit()
        return jsonify({'msg':'添加成功'})


class putCarousel(Resource):
    def put(self,id):
        parse = parser.parse_args()
        cover_img = parse.get('cover_img')
        content = parse.get('content')
        car = Carousel.query.filter(Carousel.id==id).first()
        if car:
            car.cover_img = cover_img
            car.content = content
            db.session.commit()
            return jsonify({'msg':'修改成功'})
        else:
            return jsonify({})


class delCarousel(Resource):
    def delete(self,id):
        car = Carousel.query.filter(Carousel.id==id).first()
        if car:
            db.session.delete(car)
            db.session.commit()
            return jsonify({'msg':'删除成功'})
        else:
            return jsonify({})