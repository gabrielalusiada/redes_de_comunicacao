#!/usr/bin/env python
# coding: utf-8

# ## Funções

# In[1]:


def hello():
    print("Hello!")


# In[2]:


hello()


# In[3]:


def user_age_in_seconds():
    user_age = int(input("Digite a sua idade:"))
    age_seconds = user_age*365*24*60*60
    print(f"Sua idade em segundos é {age_seconds}.")


# In[4]:


user_age_in_seconds()


# ### palavras reservadas
# ```Python
# def print():
#     print("Hello, world") # erro pois a função print é built-in
# ```

# In[5]:


# cuidado: nomes de variáveis dentro e fora da função (âmbito/escopo)

friends = ["Rolf", "Bob"]

def add_friend():
    friend_name = input("Digite o nome do seu amigo: ")
    friends = friends + [friend_name]


# In[6]:


add_friend()
print(friends)


# In[7]:


# cuidado: nomes de variáveis dentro e fora da função (âmbito/escopo)

friends = ["Rolf", "Bob"]

def add_friend():
    friends_list = ["Ted"]
    friend_name = input("Digite o nome do seu amigo: ")
    friends_list = friends_list + [friend_name]
    print(friends_list)


# In[8]:


add_friend()


# In[9]:


friends_list


# In[10]:


# é preciso definir a função antes de chamá-la

say_hello()


# In[11]:


# cuidado: nomes de variáveis dentro e fora da função (âmbito/escopo)

friends = ["Rolf", "Bob"]

def add_friend():
    #friends = ["Ted"]
    friend_name = input("Digite o nome do seu amigo: ")
    friends = friends + [friend_name]
    print(friends)


# In[12]:


add_friend()


# In[13]:


friends = ["Rolf", "Bob"]
friends = friends + ["Joao"]
print(friends)


# In[14]:


print(friends)


# In[15]:


def add_friend():
    friends.append("Rolf")
    
friends = []
add_friend()

print(friends)


# ## Argumentos e parâmetros

# In[16]:


def add(x, y): # x, y = parâmetros
    result = x + y
    print(result)


# In[17]:


add(2, 3) # 2, 3 = argumentos 


# In[18]:


# funções sem parametro não podem receber argumentos
def say_hello():
    print("Hello!")


# In[19]:


say_hello("Bob")


# In[20]:


# funções sem parametro não podem receber argumentos
def say_hello(name):
    print(f"Hello, {name}!")


# In[21]:


say_hello("Bob")


# In[22]:


say_hello()


# In[23]:


say_hello(name="Bob") # keyword


# In[24]:


def divide(dividend, divisor):
    if divisor != 0:
        print(dividend/divisor)
    else:
        print("Erro! Divisão por zero!")


# In[25]:


divide(15, 3)


# In[26]:


divide(3, 15)


# In[27]:


divide(dividend=15, divisor=3)


# In[28]:


divide(divisor=3, dividend=15)


# In[29]:


divide(15, divisor=3)


# In[30]:


divide(dividend=15, 3)


# ### Parametros com valores default
# 
# **Ordem de parâmetros opcionais ou default**
# * Primeiro parâmetros que são obrigatórios e não possuem valores default
# * Depois parâmetros com valores padrão

# In[31]:


def add(x, y=3):
    print(x + y)


# In[32]:


def add(x=4, y):
    print(x + y)


# In[33]:


add(5)


# In[34]:


add(5, 8)


# In[35]:


add(y=3)


# ## Funções que retornam valores

# In[36]:


def add(x, y):
    print(x + y)


# In[37]:


add(5, 8)


# In[38]:


result = add(5, 8)


# In[39]:


result


# In[40]:


def add(x, y):
    return x + y


# In[41]:


result = add(5, 8)


# In[42]:


print(result)


# In[43]:


def add(x, y):
    return
    print(x + y)
    return x + y


# In[44]:


add(3, 4)


# In[45]:


def divide(dividend, divisor):
    if divisor != 0:
        return dividend/divisor
    else:
        return "Erro! Divisão por zero!"


# In[46]:


result = divide(15, 3)


# In[47]:


print(result)


# In[48]:


another = divide(15, 0)
print(another)


# ### Funções lambda
# 
# * Funções curtas, que não serão reutilizadas. Geralmente usadas sem atribuir à função um nome
# * Por exemplo, usando a função map
# * map aplica a função a todos os valores de uma lista
# * quase sempre funções de uma única linha
# 

# In[49]:


def add(x, y):
    return x + y

print(add(5, 7))


# In[50]:


add_2 = lambda x, y: x + y
print(add_2(5, 7))


# In[51]:


def double(x):
    return x*2


# In[52]:


sequence = [1, 3, 5, 9]


# In[53]:


doubled = [
    double(x) for x in sequence
]
doubled


# In[54]:


doubled_2 = map(double, sequence)
print(list(doubled_2))


# In[55]:


doubled_3 = map(lambda x: x*2, sequence)


# In[56]:


list(doubled_3)


# ### Desempacotando argumentos

# In[57]:


# declarar a função para número variável de argumentos
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total


# In[58]:


multiply(3, 5)


# In[59]:


multiply(2, 3, 5)


# In[60]:


add(3, 5)


# In[61]:


nums = [3, 5]
add(*nums)


# In[62]:


nums = [3, 5, 6]
add(*nums)


# #### Desempacotando argumentos keywords

# In[63]:


# declarar a função para número variável de argumentos
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total


# In[64]:


def apply(*args, operator):
    if operator == '*':
        return multiply(args)
    elif operator == '+':
        return sum(args)
    else:
        return "Não foram passados argumentos válidos para função apply()."


# In[65]:


apply(1, 3, 6, 7, operator = "+")


# In[66]:


apply(1, 3, 7, "+")


# In[67]:


def named(**kwargs): #kw = keywords
    print(kwargs)
named(name = "Bob", age = 25)


# In[68]:


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


# In[69]:


print_nicely(name="Bob", age=25)


# In[70]:


def both(*args, **kwargs):
    print(args)
    print(kwargs)
    
both(1, 3, 5, name="Bob", age=25)


# Isto permite a criação de funções com um número ilimitado de argumentos ou de argumentos keywords
# 
# ```Python
# def post(url, data=None, json=None, **kwargs):
#     return request('post', url, data=data, json=json, **kwargs)
# ```

# In[ ]:




