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
    
db = client.PythoneMongoDb
collection = db.test_collection

Bank = db.Bank

print(client.list_database_names())

new_posts = [
    {
        "Nome":"Gustavo Pereira",
        "CPF":"001.001.001-01",
        "Endereço":"Taguatinga - Brasília/DF",
        "Tipo":"Conta Corrente",
        "Agência":"001",
        "Num":"1111111111",
        "Saldo":"R$1500.00"
    },
    {
        "Nome":"Matheus Oliveira",
        "CPF":"002.002.002-02",
        "Endereço":"Ceilândia - Brasília/DF",
        "Tipo":"Conta Corrente",
        "Agência":"002",
        "Num":"222222222",
        "Saldo":"R$10.00"
    },
    {
        "Nome":"Geovana Albuquerque",
        "CPF":"003.003.003-03",
        "Endereço":"Plano Piloto - Brasília/DF",
        "Tipo":"Conta Corrente",
        "Agência":"003",
        "Num":"333333333",
        "Saldo":"R$2000.00"
    }
]

postando = Bank.insert_many(new_posts)
print(postando.inserted_ids)

for x in Bank.find():
    pprint.pprint(x)