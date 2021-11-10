import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Item(Resource): # definimos resource

    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank.")

    @jwt_required()
    def get(self, name): # definimos o get request
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name = ?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}
        return {'message': 'Item not found'}, 404

        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name = ?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()

        if row:
            return {'message': "Já existe um item com o nome '{}' cadastrado.".format(name)}, 400

        data = Item.parser.parse_args()
        item = (name, data['price'])
        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query, item)
        connection.commit()
        connection.close()
        return {'name': name, 'price': data['price']}, 201 # 202 accepted - vou criar quando puder, verifique em alguns instantes


    def put(self, name):
        data = Item.parser.parse_args()

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items WHERE name = ?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()

        if row is None:
            item = (name, data['price'])
            query = "INSERT INTO items VALUES (?, ?)"
            cursor.execute(query, item)
            connection.commit()
        else:
            item = (data['price'], name)
            query = "UPDATE items SET price=? WHERE name=?"
            cursor.execute(query, item)
            connection.commit()
        connection.close()
        return {'name': name, 'price': data['price']}

    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "DELETE FROM items WHERE name = ?"
        result = cursor.execute(query, (name,))
        result.fetchone()

        connection.commit()
        connection.close()

        return {'message': 'Item deleted'}




class ItemList(Resource): # definimos resource
    #ItemList é uma lista de items
    def get(self): # retorna a lista de itens
        items = []
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items"
        for row in cursor.execute(query):
            items.append({'name': row[0], 'price': row[1]})
        return items
