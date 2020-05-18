from pymongo import MongoClient


class Mongo:
    def __init__(self, port):
        self.client = MongoClient(port=port)
        self.db = self.client.icmp

    def add_to_db(self, icmp_src, icmp_dest):
        business = {
            'source': icmp_src,
            'destination': icmp_dest,
        }
        result = self.db.icmp.insert_one(business)
        print('Adding src: {} dst: {} '.format(icmp_src, icmp_dest))
        print('finished adding to db... ;)')


if __name__ == "__main__":
    mongo = Mongo(27017)
    mongo.add_to_db(10000, 20000)
