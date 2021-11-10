import sqlite3

# 1o passo: conexão
connection =  sqlite3.connect('data.db') # sqlite armazenar toda informação da base de dados neste arquivo

# 2o passo: cursor
cursor = connection.cursor()

# 3o passo: queries
#create_table = "CREATE TABLE users (id int, username text, password text)"
#cursor.execute(create_table)

# armazenar dados na base de dados
#user = (1, 'joao', '1234')
#insert_query = "INSERT INTO users VALUES (?, ?, ?)"
#cursor.execute(insert_query, user)

# inserir múltiplas linhas
#users = [(2, 'gabriela', 'azul'),
#         (3, 'pedro', 'verde')]
#cursor.executemany(insert_query, users)

# como recuperamos dados
select_query = "SELECT * FROM items"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()
