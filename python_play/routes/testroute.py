# from python_play import *
# from python_play import *

import sys, os.path
sys.path.append(os.path.abspath('../../'))
from run import *

print 'inside testroute'

from python_play.classes import *
from python_play.utils import *


returnserver = MyServer()



# probably won't be able to return this (see https://stackoverflow.com/questions/21406057/flask-view-raises-typeerror-bool-object-is-not-callable)
# @app.route('/return_db', methods=['POST'])
# def return_db_request():
#     return userdbObject.return_db()


# here are some route testing functions - leave in for now (may add to)

@app.route('/getTEST', methods=['GET'])
def test():
    star = mongo.db.stars
    star_id = star.insert({'name': 'pants', 'distance': 'billions'})
    new_star = star.find_one({'_id': star_id })
    output = {'name' : new_star['name'], 'distance' : new_star['distance']}
    return jsonify({'result' : output})


@app.route('/classesTEST', methods=['GET'])
def test2():
    return returnserver.globalData

@app.route('/utilsTEST', methods=['GET'])
def test3():
    return insidehashing
