# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
#host='localhost', port=27017

class NewsappPipeline:
    def __init__(self):
        self.conn = pymongo.MongoClient(
            "mongodb+srv://dbNews:dbNews@news.heet0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = self.conn['newsdb']
        self.collection = db['news_tb']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item

