from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList
# instalar Flask-JWT
# JWT - JSON web token

app = Flask(__name__) # nada de novo
app.secret_key = 'laranja'
api = Api(app) # transformando o app em api

jwt = JWT(app, authenticate, identity) # cria o endpoint auth


# completar o código de ItemList
# implementar o método put em Item


api.add_resource(Item, '/item/<string:name>') # definimos o endpoint
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
app.run(port=5000, debug=True)

# Vamos imaginar queremos items
