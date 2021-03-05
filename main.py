import sys
# problema com o arquivo grande
sys.setrecursionlimit(2500)

def write_config(bucket_size, page_size):
    f = open("globals.py", "w")
    f.write(f'bucket_size={bucket_size}\npage_size={page_size}')
    f.close()

write_config(4, 3)

from control import Control
control = Control()
control.readfile("words.txt")
print(control.get_info())
print(control.search("quadra"))