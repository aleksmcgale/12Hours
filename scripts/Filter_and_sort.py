from queue import PriorityQueue

import nltk
from keys import keys
from pymongo import *


uri = "mongodb://johnny:apples15@ds064748.mlab.com:64748/uoft-hacks"

client = MongoClient(uri)

db = client.get_database()

items = db['items']


def jtos(json):
    res = ""
    for i in json:
        res += i['name']
        res += " "
    return res


def chew(string):
    tokens = nltk.word_tokenize(string)
    tagged = nltk.pos_tag(tokens)
    arr = []
    for (a, b) in tagged:
        if b == "NN":
            arr.append(a)
    return arr



# def extract_list(priority_entry_list):
#     new_list = []
#     for item in priority_entry_list:
#         new_list.append(item.data)
#     return new_list
#

#
# def prioritize(arr):
#     plist = []
#     # pq = PriorityQueue()
#     for i in arr:
#         if i in kvset:
#             # pq.append(PriorityEntry(collection.find(i), i))
#             plist.append(PriorityEntry(collection.find(i), i))
#     plist.sort()
#     db_entry = extract_list(plist)
#     db.priority_collection.insertOne(db_entry)


#
# def extract(pq):
#     if not pq.isEmpty():
#         a = pq.delete()
#         return a.data
#     else:
#         return 0


#
# def userconfirm(bool, item):
#     if bool:
#         if collection.find_one(item):
#             temp = collection.find_one(item)
#             new_count = {"$set": {item: temp+1}}
#             collection.update_one(item, new_count)
#         else:
#             kvs = {item:1}
#             collection.insert_one(kvs)
#
#

def json_to_tags(json):
    string = jtos(json)
    words = chew(string)
    return words[:3]




class PriorityEntry(object):

    def __init__(self, priority, data):
        self.data = data
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority