"""
database
"""

__all__ = 'Base', 'initialize', 'terminate', 'models'

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from . import models


def initialize(url='sqlite://'):
    engine = create_engine(url, convert_unicode=True)
    session = scoped_session(sessionmaker(bind=engine))
    Base.query = session.query_property()
    Base.metadata.create_all(bind=engine)
    return engine, session


def terminate(engine, session):
    session.close_all()
    engine.dispose()