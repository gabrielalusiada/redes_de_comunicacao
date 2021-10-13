from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {"name": "Minha loja",
     "items": [
         {
             'name': "Meu item",
             'price': 15.99
         }
     ]
    }
]

@app.route("/")
def home():
    return "Hello world"


# POST /store data: {name:}  - criar uma nova store com um name
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name> - retorna informações da loja name
@app.route('/store/<string:name>')
def get_store(name):
    # percorrer stores para encontrar a loja com name
    for store in stores:
        if store['name']==name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})

    # se nenhuma for encontrada, imprima uma mensagem de erro

# GET /store - retornar todas as lojas
@app.route('/store')
def get_stores():
    return jsonify(({'stores': stores}))

# POST /store/<string:name>/item {name:, price:} - cria um item em uma loja
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store():
    pass

# GET /store/<string:name>/item - retorna todos os itens de uma loja
@app.route('/store/<string:name>/item')
def get_items_in_store():
    pass


app.run(port=5000)