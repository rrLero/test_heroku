# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from sqlalchemy.ext.declarative import declarative_base
from my_models import Base, Player, Tournaments
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

if os.environ.get('DATABASE_URL') is None:
    url = "postgresql:///my_terst_base"
else:
    url = os.environ['DATABASE_URL']


engine = create_engine(url)

Base = declarative_base()
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session_git = DBSession()


@app.route('/')
def index():
    return 'Test app Postgresql on Heroku'


# Добавить запись в базу в таблицу Player
@app.route('/add/<player_name>')
def add_player(player_name):
    new_user = Player(player_name=player_name, player_surname='def', photo_path='def_photo')
    session_git.add(new_user)
    session_git.commit()
    session_git.close()
    return jsonify({'player_name': player_name})


# Удалить все записи из базы в таблице Player
@app.route('/del')
def del_player():
    query = session_git.query(Player)
    for x in query:
        session_git.delete(x)
    session_git.commit()
    session_git.close()
    return jsonify({'operation': 'deleted'})


# Прочитать таблицу и на экран
@app.route('/list')
def list_player():
    query = session_git.query(Player)
    y = []
    for x in query:
        y.append([x.player_name, x.player_surname, x.photo_path])
    return jsonify(y)


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

#
# if __name__ == '__main__':
#     app.run(debug=True)