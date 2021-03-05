import math
from db.page import Page
from db.tuplex import Tuple
from db.bucket import Bucket
from db.table import Table

class Control:
    buckets = dict()
    table = Table()
    info = {"collision": 0, "overflow": 0}

    def hash_function(self, text):
        value = str()
        for i in text:
            char_value = math.sqrt(ord(i))
            value += str(int(math.modf(char_value)[0] * 10))
        return int(value)

    def readfile(self, file):
        page = Page()
        tuples = list()
        with open(file, 'r') as reader:
            for reg in reader:
                reg = reg.replace("\n", "")
                _hash = self.hash_function(reg)
                tuples.append(Tuple(reg))
                if not page.set_register(reg):
                    page = page.next
                if _hash not in self.buckets:
                    bucket = Bucket()
                    bucket.add_ref(page)
                    self.buckets[_hash] = bucket
                else:
                    bucket = self.buckets[_hash]
                    self.info["collision"] += 1
                    bucket.add_ref(page)

                if bucket.overflow:
                    self.info["overflow"] += 1
        self.table.tuples = tuples

    def get_info(self):
        return {
             "collision": self.info["collision"],
             "overflow": self.info["overflow"]
        }

    def search(self, text):
        cost = int()
        index = self.hash_function(text)
        bucket = self.buckets[index]
        while bucket is not None:
            for page in bucket.pages:
                for reg in page.register:
                    cost += 1
                    if reg == text:
                        return cost, reg
            bucket = bucket.next_bucket
