import datetime
import pprint

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Conectando ao servidor do mongdb
uri = "mongodb+srv://gugubmb:mugiwara356248@cluster0.18lo9ix.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Seleciona ou cria se não existir meu banco de dados desejado
db = client.test
collection = db.test_collection

# Usado para incluir os documentos no banco de dados (mas para criar precis)
posts = db.posts

# Exibe a lista de banco de dados
# print(client.list_database_names())

# # Declarando apenas um documento
# post = {
#     "author":"GGGG",
#     "text":"My first mongodg application based on python",
#     "tags":["mongodb", "python", "pymongo"],
#     "date":datetime.datetime.utcnow()
# }

# # Incluindo no banco de dados o domento de post
# post_id = posts.insert_one(post).inserted_id

# Busca e exibe o primerio documento
# print(db.posts.find_one())
# print()
# pprint.pprint(db.posts.find_one())

# Declarando varios documentos
# new_posts = [{
#     "author":"Mustafá",
#     "text":"Negurezin é bom",
#     "tags":["bom", "arábe"],
#     "date":datetime.datetime.utcnow()
#     },
#     {
#     "author":"Pedro",
#     "text":"Post é tu",
#     "title":"Mongo is fun",
#     "date":datetime.datetime.utcnow()
#     }]

# Incluindo no banco de dados os documetos de new_posts
# result = posts.insert_many(new_posts)
# print(result.inserted_ids)

# Exibe o documento com nome Pedro
# pprint.pprint(db.posts.find_one({"author":"Pedro"}))

# Exibe todos os documentos em posts
# for post in posts.find():
#     pprint.pprint(post)

# Exibe todas as minhas coleçoes 
# collections = db.list_collection_names()
# for x in collections:
#     print(x)

# Exclui uma coleção inteira no meu banco de dados
# db['profile_user'].drop()

# result = db.posts.find( {"author": "aaaa"} )
# for x in result:
#     print(x)
