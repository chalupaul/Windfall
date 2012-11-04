import os, sys, re, yaml, bottle
from bottle.ext.sqlalchemy import SQLAlchemyPlugin
from sqlalchemy import create_engine, Column, Integer, Sequence, String
from sqlalchemy.ext.declarative import declarative_base
import globals

load_dir = os.path.dirname(os.path.realpath(__file__))

sys.path = [load_dir] + sys.path
os.chdir(load_dir)


app_base = os.path.dirname(os.path.realpath(__file__))
app_base_join = lambda x: os.path.join(os.sep, app_base, x)


#Bottle template path and config
bottle.TEMPLATE_PATH.append(app_base_join('views'))
configs = yaml.load(open(app_base_join('conf' + os.sep + "application.yaml")))


#SQL Alchemy
engine = create_engine(configs['database'][configs['environment']]['conn_string'], echo=False)
globals.Base = declarative_base()
print "Creating Base"


#Import windfall structure
control_dirs = ['errors', 'services', 'models', 'controllers'  ]
[sys.path.append(dir) for dir in control_dirs]
[__import__(file[:-3]) 
 for cdir in control_dirs 
 for file in os.listdir(app_base_join(cdir))
   if re.match('.*_' + cdir[:-1] + '.py$', file)]

if configs['environment'] == 'dev':
    globals.Base.metadata.create_all(engine)
    
print "installing plugin"
bottle.install(SQLAlchemyPlugin(engine, globals.Base.metadata, create=True))


#Get host of api server from config
globals.API_SERVER_IP = configs['api_server'][configs['environment']]['host'] + ":" + configs['api_server'][configs['environment']]['port']

   
    
if __name__ == '__main__':
    bottle.debug(True)
    #bottle.run(reloader=True)
    bottle.run(host=configs['api_server'][configs['environment']]['host'], port=configs['api_server'][configs['environment']]['port'])
else:
     # Mod WSGI launch
    print "MOD WSGI"
    os.chdir(os.path.dirname(__file__))
    application = bottle.default_app()
