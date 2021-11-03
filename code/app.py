from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity
from user import UserRegister
# instalar Flask-JWT
# JWT - JSON web token

app = Flask(__name__) # nada de novo
app.secret_key = 'laranja'
api = Api(app) # transformando o app em api

jwt = JWT(app, authenticate, identity) # cria o endpoint auth

items = []

class Item(Resource): # definimos resource

    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank.")

    @jwt_required()
    def get(self, name): # definimos o get request
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "Já existe um item com o nome '{}' cadastrado.".format(name)}, 400

        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201 # 202 accepted - vou criar quando puder, verifique em alguns instantes


    def put(self, name):
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name']!=name, items))
        return {'message': 'Item deleted'}


class ItemList(Resource): # definimos resource
    #ItemList é uma lista de items
    def get(self): # retorna a lista de itens
        return items


# completar o código de ItemList
# implementar o método put em Item


api.add_resource(Item, '/item/<string:name>') # definimos o endpoint
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
app.run(port=5000, debug=True)

# Vamos imaginar queremos items
