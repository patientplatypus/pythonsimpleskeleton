
# from python_play import *

import sys, os.path
sys.path.append(os.path.abspath('../../'))
from run import *


from python_play.classes import *
from python_play.utils import *


userinfoObject = UserINFO()

@app.route('/show_db', methods=['GET'])
def show_db_request():
    userinfoObject.show_db()
    return 'garbage'
