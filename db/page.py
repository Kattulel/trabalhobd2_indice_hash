import globals

class Page:
    def __init__(self):
        self.max_size = globals.page_size
        self.register = list()
        self.next = None

    def set_register(self, text):
        size = len(self.register)
        if size < self.max_size:
            self.register.append(text)
            return True
        else:
            new_page = Page()
            new_page.set_register(text)
            self.next = new_page
            return False
