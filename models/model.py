

from datetime import datetime

import sqlalchemy
import sqlalchemy.ext.declarative

from sqlalchemy import Column, Sequence, Integer, String, Boolean, DateTime, Text, Enum, ForeignKey
from sqlalchemy.orm import relationship, backref


Base = sqlalchemy.ext.declarative.declarative_base()

class User(Base):
  __tablename__ = 'user'
  id = Column(Integer, Sequence('user_id_sqq'), primary_key=True)
  screen_name = Column(String(12))
  name = Column(String(12))
  image = Column(String(128))
  nickname = Column(String(12))
  created = Column(DateTime)
  modified = Column(DateTime)
  def __init__(self, student_no, name, image, nickname, department):
    self.student_no = student_no
    self.name = name
    self.image = image
    self.nickname = nickname
    self.department = department
    self.created = datetime.now()
    self.modified = datetime.now()


class Wonder(Base):
  __tablename__ = "wonder"
  id = Column(Integer, Sequence('wonder_id_sqq'), primary_key=True)
  polite_id = Column(String(12), unique=True)
  name = Column(String(64))
# relation for foreign key
  discussion_tool = relationship("DiscussionTool", backref="course")
# Meta data
  created = Column(DateTime)
  modified = Column(DateTime)
  def __init__(self, polite_id, name, status):
    self.polite_id = polite_id
    self.name = name
    self.status = status
    self.created = datetime.now()
    self.modified = datetime.now()

class Note(Base):
  __tablename__ = "note"



# FOR DEBUG #
url = 'sqlite://'
engine = sqlalchemy.create_engine(url, echo=True)
Base.metadata.create_all(engine)


