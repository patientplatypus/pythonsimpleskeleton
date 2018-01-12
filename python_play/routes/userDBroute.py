



# from python_play.classes import *
# from python_play import *

import sys, os.path
sys.path.append(os.path.abspath('../../'))
from run import *


from python_play.classes import *
from python_play.utils import *


userdbObject = UserDB()



@app.route('/add_user', methods=['POST'])
def add_user_request():
    print 'inside add_user route'
    username = request.json['username']
    password = request.json['password']
    returnval = userdbObject.add_user(username, password)
    if returnval == True:
        return 'True'
    else:
        return 'False'

@app.route('/delete_user', methods=['POST'])
def delete_user_request():
    username = request.json['username']
    password = request.json['password']
    returnval = userdbObject.delete_user(username, password)
    if returnval == True:
        return 'True'
    else:
        return 'False'


@app.route('/find_user', methods=['POST'])
def find_user_request():
    username = request.json['username']
    password = request.json['password']
    returnval = userdbObject.find_user(username, password)
    if returnval == True:
        return 'True'
    else:
        return 'False'

@app.route('/login_logout', methods=['POST'])
def login_logout_request():
    username = request.json['username']
    password = request.json['password']
    loginlogout = request.json['loginlogout']
    returnval =  userdbObject.login_logout(username, password, loginlogout)
    if returnval == True:
        return 'True'
    elif returnval == False:
        return 'False'
    else:
        return returnval
