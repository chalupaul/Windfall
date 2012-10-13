import os, sys, re, yaml, bottle

from bottle.ext import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, Sequence, String
from sqlalchemy.ext.declarative import declarative_base

app_base = os.path.dirname(os.path.realpath(__file__))
app_base_join = lambda x: os.path.join(os.sep, app_base, x)



#Bottle template path and config
bottle.TEMPLATE_PATH.append(app_base_join('views'))
configs = yaml.load(open(app_base_join('conf' + os.sep + "application.yaml")))


#SQL Alchemy
engine = create_engine(configs['database'][configs['environment']]['conn_string'], echo=True)
Base = declarative_base()

#Import windfall structure
control_dirs = ['controllers', 'errors', 'models', 'services']
[sys.path.append(dir) for dir in control_dirs]
[__import__(file[:-3]) 
 for cdir in control_dirs 
 for file in os.listdir(app_base_join(cdir))
   if re.match('.*_' + cdir[:-1] + '.py$', file)]

if configs['environment'] == 'dev':
    Base.metadata.create_all(engine)
    
bottle.install(sqlalchemy.Plugin(engine, Base.metadata, create=True))


   
    
if __name__ == '__main__':
    bottle.debug(True)
    bottle.run(reloader=True)
else:
    bottle.run(host='localhost')

