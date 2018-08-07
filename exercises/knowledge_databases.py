from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(topic,article,rating):
	knowledge_object=Knowledge(
		topic=topic,
	    article=article,
		rating=rating)
	session.add(knowledge_object)
	session.commit()

add_article("food", "what is a genetically modified crop", 8)
add_article("weather", "rain wikipedia", 5)
add_article("dogs", "dog adoption", 10)

def query_all_articles():
	knowledge=session.query(Knowledge).all()
	return knowledge

print(query_all_articles())

def query_article_by_topic(their_topic):
	knowledge=session.query(Knowledge).filter_by(topic=their_topic).first()
	return knowledge

print(query_article_by_topic("dogs"))

def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(topic=topic).delete()
	session.commit()

delete_article_by_topic("weather")	
print(query_all_articles())

def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()

delete_all_articles()
print(query_all_articles())

def edit_article_rating():
	pass



