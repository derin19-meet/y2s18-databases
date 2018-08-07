from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__="knowledge"
	knowledge_id=Column(Integer, primary_key=True)
	article=Column(String)
	topic=Column(String) 
	rating=Column(Integer)
	

	def __repr__(self):
		return( 
			"if you want to learn more about :{}\n"
			"you should look at the article called:{}\n"
			"and our rating of that article is:{}\n").format(
				#self.knowledge_id,
				self.topic,
				self.article,
				self.rating
				)

# print(repr(Knowledge.__table__))					

x=Knowledge(topic="food", article="gmo", rating=8)
y=Knowledge(topic="weather", article="rain", rating=5)
print(x)
print(y)









