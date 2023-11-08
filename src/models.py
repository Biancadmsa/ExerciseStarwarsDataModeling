# import os
# import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
# from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False, unique=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    favorites =  relationship('favorite')

class Persons(Base):
    __tablename__ = 'Persons'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    birth_Year = Column(String(20))
    skin_color = Column(String(80))
    height = Column(String(8))
    eye_color = Column(String(8))
    favorites =  relationship('favorite')

class Planets(Base):
    __tablename__ = 'Planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    climate = Column(String(20))
    population = Column(Integer)
    orbital_period = Column(String(8))
    rotate_period = Column(String(8))
    favorites =  relationship('favorite')
    
class Favorite(Base):
    __tablename__ = "favorite"    
    id = Column(Integer, primary_key=True)
    #Personaje
    persons = relationship(Persons)
    persons_id = Column(Integer, ForeignKey('Persons.id'), nullable=True)
    
    #Planeta
    planets = relationship(Planets)
    planets_id = Column(Integer, ForeignKey('Planets.id'), nullable = True)

    #Usuario
    user_id = Column(Integer, ForeignKey('User.id'), nullable= False)
    user = relationship(User)

    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')