


# from python_play import *

# good inheritance reference http://introtopython.org/classes.html#Inheritance-in-Python-2.7

from userDBclass import *

class UserINFO(UserDB):

    def __init__(self):
        super(UserINFO, self).__init__()

    def show_db(self):
        print 'inside show_db'
        cursor = self.database.find({})
        for document in cursor:
              print(document)
