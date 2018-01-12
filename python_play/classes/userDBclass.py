

import sys, os.path
sys.path.append(os.path.abspath('../../'))
from run import *

# from python_play import *
# hash after checking can add to database

from python_play.utils import *


class UserDB(object):

    def __init__(self):
        self.database = mongo.db.database

    def find_user(self, username):
        checkuser = self.database.find_one({'username': username})
        if checkuser is None:
            return False
        else:
            return checkuser

    def add_user(self, username, password):
        # print 'inside add_user def'
        userexists = self.find_user(username)
        # print 'value of userexists'
        print userexists
        if userexists==False:
            hashedpassword = generate_password_hash(password)
            self.database.insert({'username': username, 'password': hashedpassword, 'login': False})
            return True
        else:
            return False

    def delete_user(self, username, password):
        checkuser = self.find_user(username)
        if checkuser != False:
            self.database.delete_one({'username': username, 'password': password})
            return True
        else:
            return False

    def login_logout(self, username, password, loginlogout):
        # print 'inside login_logout'
        # print '******************'
        # return "True"
        checkuser = self.find_user(username)


        if checkuser != False:
            print 'value of verify_password_hash(password, checkuser[password]) in loginlogout'
            print verify_password_hash(password, checkuser['password'])
            if verify_password_hash(password, checkuser['password']) == True:
                result = self.database.update_one({'username': username, 'password': password, 'login': loginlogout}, {'$set': {'username': username, 'password': password, 'login': not loginlogout}})
                print not loginlogout
                return not loginlogout
            if verify_password_hash(password, checkuser['password']) == False:
                print "didnotverifypassword"
                return "didnotverifypassword"
        else:
            print 'didnotfinduser'
            return "didnotfinduser"

    def return_db(self):
        return self.database

    def show_db(self):
        print 'inside show_db'
        cursor = self.database.find({})
        for document in cursor:
              print(document)
