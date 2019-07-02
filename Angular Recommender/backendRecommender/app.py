# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 22:28:41 2019

@author: hedi
"""

from flask import Flask
import json
from Recommender import getRecommendedItems
import databaseCon


app= Flask(__name__)

@app.route("/predictions/<int:uid>",strict_slashes=False)


def predictions(uid):
    return json.dumps(getRecommendedItems(uid),indent=2)

@app.route("/CreateUser/<string:uid>",strict_slashes=False)

def createUser(uid):
    con= databaseCon.Database()
    return con.CreatetUser(uid)


@app.route("/GetUser/<string:uid>",strict_slashes=False)

def GetUser(uid):
    con= databaseCon.Database()
    return json.dumps(con.getUser(uid),indent=2)


@app.route("/GetNameRest/<string:uid>",strict_slashes=False)

def GetNameRest(uid):
    con= databaseCon.Database()
    return json.dumps(con.getRestoName(),indent=2)

@app.route("/RateRestaurants/<string:Restaurantid>/<int:value>/<string:uid>",strict_slashes=False)

def RateRestaurant(Restaurantid,value,uid):
    con= databaseCon.Database()
    return con.RateRestaurant(Restaurantid,value,uid)


@app.route("/GetNearRest/<string:uid>",strict_slashes=False)

def GetNearRest(uid):
    con= databaseCon.Database()
    return json.dumps(con.NearRestaurants(uid),indent=2)

if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)