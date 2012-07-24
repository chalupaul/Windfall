import sys, os, bottle
load_dir = os.path.dirname(os.path.realpath(__file__))

sys.path = [load_dir] + sys.path
os.chdir(load_dir)
print load_dir
import Windfall
application = bottle.default_app()


