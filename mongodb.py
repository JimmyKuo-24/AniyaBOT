from pymongo import MongoClient
import urllib.parse, datetime, EXRate
from line_bot import *

currency_list = {
        'AUD': '澳幣',  
        'CAD': '加拿大幣',
        'CHF': '瑞士法郎',
        'CNY': '人民幣',
        'EUR': '歐元',
        'GBP': '英鎊',
        'HKD': '港幣',
        'IDR': '印尼幣',
        'JPY': '日元',
        'KRW': '韓元',
        'MYR': '馬來幣',
        'NZD': '紐元',
        'PHP': '菲律賓幣',
        'SEK': '瑞典克朗',
        'SGD': '新加坡幣',
        'THB': '泰銖',
        'USD': '美元',
        'VND': '越南盾',
    }

Authdb = 'test-good1'
stockDB = 'mydb'
currencyDB = 'users'
dbname = 'test-good1'

def constructor_stock():
    client = MongoClient('mongodb://s30305301:zgHbQAYmcnl2ieJ7@ac-77dgnl6-shard-00-00.axxs3vy.mongodb.net:27017,ac-77dgnl6-shard-00-01.axxs3vy.mongodb.net:27017,ac-77dgnl6-shard-00-02.axxs3vy.mongodb.net:27017/?ssl=true&replicaSet=atlas-1uu9mw-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0')
    db = client[stockDB]
    return db

def constructor_currency():
    client = MongoClient('mongodb://s30305301:zgHbQAYmcnl2ieJ7@ac-77dgnl6-shard-00-00.axxs3vy.mongodb.net:27017,ac-77dgnl6-shard-00-01.axxs3vy.mongodb.net:27017,ac-77dgnl6-shard-00-02.axxs3vy.mongodb.net:27017/?ssl=true&replicaSet=atlas-1uu9mw-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0')
    db = client[currencyDB]
    return db

def write_my_stock(userID, user_name, stockNumber, condition, target_price):
    db = constructor_stock()
    collect = db[user_name]
    is_exit = collect.find_one({'favorite_stock': stockNumber})
    if is_exit != None:
        content = update_my_stock(user_name, stockNumber, condition, target_price)
        return content
    else:
        collect.insert_one({'userID': userID, 'favorite_stock': stockNumber, 'condition': condition, 'target_price': target_price,
                            'tag': 'stock', 'date_info':datetime.datetime.now()})
        return f'{stockNumber}已加入追蹤清單'

def update_my_stock(user_name, stockNumber, condition, target_price):
    db = constructor_stock()
    collect = db[user_name]
    collect.update_many({'favorite_stock': stockNumber}, {'$set': {'condition': condition, 'price': target_price}})
    content = f'{stockNumber}已更成功'
    return content

def show_my_stock(user_name, userID):
    db = constructor_stock()
    collect = db[user_name]
    dataList = list(collect.find({'userID': userID}))
    if dataList == []:
        return '尚未追蹤任何股票'
    content = '您清單的選股條件如下：\n'
    for i in range(len(dataList)):
        content += f"{dataList[i]['favorite_stock']}  {dataList[i]['condition']}  {dataList[i]['price']}\n"
    return content

def delete_my_stock(user_name, stockNumber):
    db = constructor_stock()
    collect = db[user_name]
    collect.delete_one({'favorite_stock': stockNumber})
    return stockNumber + '刪除成功'

def delete_my_allstock(user_name, userID):
    db = constructor_stock()
    collect = db[user_name]
    collect.delete_one({'userID': userID})
    return '所有股票刪除成功'

def update_my_currency(user_name, currency, condition, target_price):
    db = constructor_currency()
    collect = db[user_name]
    collect.update_many({'favorite_currency': currency}, {'$set': {'condition': condition, 'price': target_price}})
    return f'{currency_list[currency]}更新成功'

def write_my_currency(userID , user_name, currency, condition, target_price):
    db = constructor_currency()
    collect = db[user_name]
    is_exit = collect.find_one({"favorite_currency": currency})
    content = ""
    if is_exit != None : return update_my_currency(user_name, currency, condition , target_price)
    else:
        collect.insert_one({
                "userID": userID,
                "favorite_currency": currency,
                "condition" :  condition,
                "price" : target_price,
                "tag": "currency",
                "date_info": datetime.datetime.now()
            })
        return f"{currency_list[currency]}已新增至您的外幣清單"
    
def show_my_currency(userID, user_name):
    db = constructor_currency()
    collect = db[user_name]
    dataList = list(collect.find({"userID": userID}))
    if dataList == [] : return "您的外幣清單為空，請透過指令新增外幣至清單中"
    content = ""
    for i in range(len(dataList)):
        content += EXRate.showCurrency(dataList[i]["favorite_currency"])
    return content

def delete_my_currency(user_name, currency):
    db = constructor_currency()
    collect = db[user_name]
    collect.delete_one({"favorite_currency": currency})
    return currency_list[currency] + "刪除成功"

def delete_my_allcurrency(user_name, userID):
    db = constructor_currency()
    collect = db[user_name]
    collect.delete_many({"userID": userID})
    return "外幣清單刪除成功"
    
