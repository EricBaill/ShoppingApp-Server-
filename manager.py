# -*- coding: utf-8 -*-
import json

from flask import request, jsonify
from flask_migrate import MigrateCommand
from flask_restful import reqparse
from flask_script import Manager
from App import create_app
from utrils.aliyunsms.sms_send import send_sms
import random

app = create_app('develop')

manager = Manager(app=app)
manager.add_command('db',MigrateCommand)


from qiniu import Auth, put_data
# 用户上传到服务器，服务器再上传到七牛云

parser = reqparse.RequestParser()
parser.add_argument(name='phone',type=str)


@app.route("/uploadImg", methods=["GET", "POST"])
def upload_qiniu():
    fp = request.files.get("file")
    file_name = fp.filename

    # 需要填写你的 Access Key 和 Secret Key
    ak = "x8Wiq7iIUk3mZnuKDG2A5y14HLIHieMYZK3UsJJT"
    sk = "sYQit3y31B9VIL-vQkUho9toQn0noLcf-UFihcQZ"
    # 构建鉴权对象
    q = Auth(ak, sk)
    # 要上传的空间
    bucket_name = 'cloudprint'
    # 上传到七牛后保存的文件名
    key = 'shop' + '/' + 'files' + '/' + file_name
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)
    ret, info = put_data(token, key, data=fp.read())
    # 如果上传成功
    if info.status_code == 200:
        # 数据库保存该地址
        img_url = "https://www.jianxinshanghai.com/" + ret.get("key") #七牛云域名（注意：CNAME一定要配置）
        print(img_url)
    return '/'+key


@app.route("/sendsms", methods=["POST"])
def sms_captcha():
    parse = parser.parse_args()
    phone = parse.get('phone')
    str = ""
    for i in range(6):
        ch = chr(random.randrange(ord('0'), ord('9') + 1))
        str += ch
    print(str)
    params = {'code': str} #abcd就是发发送的验证码，code就是模板中定义的变量
    result = send_sms(phone, json.dumps(params))
    print(result)
    if result:
        return jsonify(params)
    else:
        return '发送失败'


if __name__ == '__main__':

    # manager.run()
    app.run(host='0.0.0.0',port='5000')
