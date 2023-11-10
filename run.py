import pymongo

myclient = pymongo.MongoClient('mongodb://usename:password@IP:27017')
db = myclient['test']    #数据库
collection = db['cars']  #集合

#插入数据:
car={'name': 'Audi', 'price': 50000}
cars = [{'name': 'Audi', 'price': 51523},
    {'name': 'Mercedes', 'price': 57127},
    {'name': 'Skoda', 'price': 9000},
    {'name': 'Volvo', 'price': 29000},
    {'name': 'Bentley', 'price': 350000},
    {'name': 'Citroen', 'price': 21000},
    {'name': 'Hummer', 'price': 42400},
    {'name': 'Hummer', 'price': 41400},
    {'name': 'Volkswagen', 'price': 21600} ]
collection.insert_one(car)
collection.insert_many(cars)
#查询数据:交集，排序，取前几
num=collection.estimated_document_count()
print('共有',num,'条数据')
onedata=collection.find_one({'name': 'Audi'})
print('\n查询单条数据')
print(onedata)
print('\n查询多条数据')
for i in collection.find():
    print(i['_id'],i['name'],i['price'])
result = collection.find({ "$and":[ {'name':'Audi'} , {'price':50000} ] }).sort('price',-1).limit(5)
print('\n按条件查询数据')
for i in result:
    print(i['_id'],i['name'],i['price'])
#修改数据
collection.update_one( {'name':'Skoda'} , {'$set':{'price':9900}})
collection.update_many( {'name':'Hummer'} , {'$set':{'price':44000}})
print('\n修改数据')
for i in collection.find({ "$or":[ {'name':'Skoda'} , {'name':'Hummer'} ] }):
    print(i)
#删除数据
collection.delete_one({'name': 'Volvo'})
collection.delete_many({'name': 'Audi'})
print('\n删除数据')
for i in collection.find():
    print(i)
#删除集合
collection.drop()
