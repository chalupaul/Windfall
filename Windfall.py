import os, sys, re, yaml, bottle

from bottle.ext.sqlalchemy import SQLAlchemyPlugin

from sqlalchemy import create_engine, Column, Integer, Sequence, String
from sqlalchemy.ext.declarative import declarative_base

app_base = os.path.dirname(os.path.realpath(__file__))
app_base_join = lambda x: os.path.join(os.sep, app_base, x)
 
configs = yaml.load(open(app_base_join('conf' + os.sep + "application.yaml")))
engine = create_engine(configs['database'][configs['environment']]['conn_string'], echo=True)
Base = declarative_base()

#plugin = sqlalchemy.Plugin(engine, Base.metadata, create=True)
#app = bottle.default_app()
#app.install(plugin)

bottle.TEMPLATE_PATH.append(app_base_join('views'))

control_dirs = ['controllers', 'errors', 'models']
[sys.path.append(dir) for dir in control_dirs]

#print sys.path

[__import__(file[:-3]) 
 for cdir in control_dirs 
 for file in os.listdir(app_base_join(cdir))
   if re.match('.*_' + cdir[:-1] + '.py$', file)]

if configs['environment'] is 'dev':
    Base.metadata.create_all(engine)

bottle.install(SQLAlchemyPlugin(engine, Base.metadata, create=True))


   
    
if __name__ == '__main__':
    bottle.debug(True)
    bottle.run(reloader=True)
else:
    bottle.run()

