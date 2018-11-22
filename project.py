import os

#from library.basic import app
from library.movie_routing import app

if __name__ == '__main__':
   app.debug = True
   app.run(host='localhost')

