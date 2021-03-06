from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from os import environ
import yaml
if 'DCHK_ENV' not in environ:
    environ['DCHK_ENV'] = 'development'

def init(engine):
    global Base
    global db_session
    Base = declarative_base()
    db_session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

def get_new_engine():
    from sqlalchemy import create_engine
    print get_db_connection_string()
    return create_engine(get_db_connection_string())

def get_db_connection_string():
    with open('config/config.yml', 'r') as f:
        config = yaml.load(f)

    conf = config['database'][environ['DCHK_ENV']]

    if 'username' in conf:
        user = conf['username']
    else:
        user = ''

    if 'password' in conf:
        user += ':{}'.format(conf['password'])

    if user != '':
        user += '@'

    #dialect+driver://username:password@host:port/database

    return '{}://{}{}{}/{}'.format(conf['type'],
                                   user,
                                   conf['host'],
                                   (':{}'.format(conf['port']) if 'port' in conf else ''),
                                   conf['database'])

if __name__ == '__main__':
    import models.helpers.base
    engine = get_new_engine()
    models.helpers.base.init(engine)
    import models.data_source
    import models.check
    import models.job_run
    import models.schedule
    import models.rule
    import models.job_template
    import models.log
    models.helpers.base.Base.metadata.create_all(engine)
    print "done"
