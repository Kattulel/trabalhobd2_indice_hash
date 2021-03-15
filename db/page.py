import globals
from db.tuplex import Tuple

class Page:
    def __init__(self):
        self.max_size = globals.page_size
        self.register = list()
        self.head = None
        self.next = None

    def set_register(self, text):
        size = len(self.register)
        if size < self.max_size:
            _tuple = Tuple(text)
            self.register.append(_tuple)
            return True
        else:
            new_page = Page()
            new_page.set_register(text)
            self.next = new_page
            return False
