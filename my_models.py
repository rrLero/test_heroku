# -*- coding: utf-8 -*-
from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Player(Base):
    __tablename__ = 'player'
    id = Column(Integer, primary_key=True)
    player_name = Column(String)
    player_surname = Column(String)
    photo_path = Column(String)
    # relationships
    lnk_tournaments_players = relationship('Tournaments')


class Tournaments(Base):
    __tablename__ = 'tournaments'
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('player.id'), nullable=False)
    place = Column(Integer, nullable=False)
    points = Column(Integer, nullable=False)