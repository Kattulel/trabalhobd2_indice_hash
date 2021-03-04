import math
from page import Page
from tuplex import Tuple
from bucket import Bucket


def hash_function(text):
    value = str()
    for i in text:
        char_value = math.sqrt(ord(i))
        value += str(int(math.modf(char_value)[0] * 10))
    return int(value)

colision = 0
buckets = dict()
tuplas = list()
page = Page()
with open('smallwords.txt', 'r') as reader:
    for reg in reader:
        reg = reg.replace("\n", "")
        _hash = hash_function(reg)
        tuplas.append(Tuple(reg))
        if not page.set_register(reg):
            page = page.next
        if _hash not in buckets:
            bucket = Bucket()
            bucket.add_ref(page)
            buckets[_hash] = bucket
        else:
            bucket = buckets[_hash]
            colision += 1
            bucket.add_ref(page)

print("x")

x = hash_function("differ")
print(buckets[x].pages[0].register)
