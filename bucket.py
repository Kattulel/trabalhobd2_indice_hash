import globals
class Bucket:
    def __init__(self):
        self.pages = list()
        self.size = 0
        self.next_bucket = None

    def is_max(self):
        return (globals.bucket_size - 1) < self.size

    def add_ref(self, page):
        if not self.is_max():
            self.pages.append(page)
            self.size +=1
        else:
            if self.next_bucket is None:
                new_bucket = Bucket()
                new_bucket.add_ref(page)
                self.next_bucket = new_bucket
            else:
                bucket = self.next_bucket
                bucket.add_ref(page)
