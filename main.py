from tinydb import TinyDB, Query
import requests

def add():
    db = TinyDB('db.json')
    url = 'http://127.0.0.1:8000/add/'
    db.default_table_name = 'Redmi'
    for i in db.all():
        dict_post = {}
        dict_post['name'] =i.get('name')
        dict_post['company'] =i.get('company')
        dict_post['color']= i.get('color')
        dict_post['RAM']=i.get('RAM')
        dict_post['memory']=i.get('memory')
        dict_post['price']=i.get('price')
        dict_post['img_url']=i.get('img_url')
        r = requests.post(url, data=dict_post)
    return db.all()
add()