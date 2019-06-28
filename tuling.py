import itchat
from itchat.content import *
import json
import requests
import apikey


@itchat.msg_register([TEXT])
def text_reply(msg):
    info = msg['Text'].encode('utf-8')
    url = 'http://www.tuling123.com/openapi/api'
	# 在"key"后填入自己机器人的apikey
    data = {u"key": apikey.apikey, "info": info, u"loc": "", "userid": ""}
    response=requests.post(url,data).content
    s = json.loads(response, encoding='utf-8')
    print('s == %s' % s)
    if s['code'] == 100000:
        itchat.send(s['text'], msg['FromUserName'])

itchat.auto_login(hotReload=True)
itchat.run(debug=True)