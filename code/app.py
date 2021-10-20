from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__) # nada de novo
api = Api(app) # transformando o app em api

items = []

class Item(Resource): # definimos resource
    def get(self, name): # definimos o get request
        for item in items:
            if item['name']==name:
                return item

    def post(self, name):
        item = {'name': name, 'price': 17}
        items.append(item)

class ItemList(Resource): # definimos resource
    #ItemList é uma lista de items
    def get(self, name): # retorna a lista de itens




api.add_resource(Item, '/item/<string:name>') # definimos o endpoint
api.add_resource(ItemList, '/items')

app.run(port=5000)

# Vamos imaginar queremos items
