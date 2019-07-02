# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 15:05:18 2019

@author: hedi
"""

import os
import csv
import sys
from surprise import Reader
from surprise import Dataset
from collections import defaultdict


class Reviews:
    
    
    dataPath = 'C:\\Users\\hedi\\Desktop\\Graduation project\\Project\\reviews.csv'
    placePath = 'C:\\Users\\hedi\\Desktop\\Graduation project\\Project\\reviewsOrg.csv'
    TestPath = 'C:\\Users\\hedi\\Desktop\\Graduation project\\Project\\reviewsTest.csv'
    DistPath = 'C:\\Users\\hedi\\Desktop\\Graduation project\\Project\\AllPossibleDistances.csv'
    DistRes ='C:\\Users\\hedi\\Desktop\\Graduation project\\Project\\ResDistances.csv'


    placeID_to_name = {}
    name_to_placeID = {}

    
    def loadRevDataSet(self):

        # Look for files relative to the directory we are running from
        os.chdir(os.path.dirname(sys.argv[0]))

        ratingsDataset = 0
        self.placeID_to_name = {}
        self.name_to_placeID = {}
        self.distance = {}
        self.dress = {}

        reader = Reader(line_format='user item rating timestamp', sep=',', skip_lines=1)

        ratingsDataset = Dataset.load_from_file(self.dataPath, reader=reader)

        with open(self.placePath, newline='', encoding='ISO-8859-1') as csvfile:
                RestReader = csv.reader(csvfile)
                next(RestReader)  #Skip header line
                for row in RestReader:
                    placeID = int(row[1])
                    placeName = row[9]
                   # distances= float(row[18])
                   # dersses= row[12]
                    
                    self.placeID_to_name[placeID] = placeName
                    self.name_to_placeID[placeName] = placeID


        return ratingsDataset



    def getPopularityRanks(self):
        ratings = defaultdict(int)
        rankings = defaultdict(int)
        with open(self.dataPath, newline='') as csvfile:
            ratingReader = csv.reader(csvfile)
            next(ratingReader)
            for row in ratingReader:
                placeID = int(row[1])
                ratings[placeID] += 1
        rank = 1
        for placeID, ratingCount in sorted(ratings.items(), key=lambda x: x[1], reverse=True):
            rankings[placeID] = rank
            rank += 1
        return rankings




    
    def getUserRatings(self, user):
        userRatings = []
        hitUser = False
        with open(self.dataPath, newline='') as csvfile:
            ratingReader = csv.reader(csvfile)
            next(ratingReader)
            for row in ratingReader:
                userID = int(row[0])
                if (user == userID):
                    placeID = str(row[1])
                    rating = float(row[2])
                    userRatings.append((placeID, rating))
                    hitUser = True
                if (hitUser and (user != userID)):
                    break

        return userRatings
    
    
    def getDistancesByRestaurant(self, user):
        distance = []
        hitUser = False
        with open(self.dataPath, newline='') as csvfile:
            ratingReader = csv.reader(csvfile)
            next(ratingReader)
            for row in ratingReader:
                userID = int(row[0])
                if (user == userID):
                    placeID = str(row[1])
                    distances= float(row[3])
                    distance.append((placeID, distances))
                    hitUser = True
                if (hitUser and (user != userID)):
                    break

        return distance
    
    def getAllPossibleDistances(self):
        
        distances = []
        with open(self.DistPath, newline='') as csvfile:
            ratingReader = csv.reader(csvfile)
            next(ratingReader)
            for row in ratingReader:
                userID = int(row[0])
                restaurantID = int(row[3])
                distance= float(row[6])
                distances.append((userID,restaurantID,distance))
        return distances 
    
    
    def getusers(self):
        
        users = []
        with open(self.dataPath, newline='') as csvfile:
            ratingReader = csv.reader(csvfile)
            next(ratingReader)
            for row in ratingReader:
                userID = int(row[0])
                if userID not in users:
                    users.append((userID))
        return users
    
    def getRestDist(self):
        
        restDist = []
        with open(self.DistRes, newline='') as csvfile:
            ratingReader = csv.reader(csvfile)
            next(ratingReader)
            for row in ratingReader:
                
                dist = float(row[6])
                restDist.append((dist))
        return restDist 
    
    def getRestDisDiff(self,place1,place2):
        
        restDistDiff = []
        with open(self.DistRes, newline='') as csvfile:
            ratingReader = csv.reader(csvfile)
            next(ratingReader)
            for row in ratingReader:
                placex=int(row[0])
                placey=int(row[3])
                if ((place1 == placex) and (place2 == placey)):
                    dist = float(row[6])
                    restDistDiff.append((dist))
        return restDistDiff 
    
    
    
    
    
    def getSmokers(self):
        
        Smokers = defaultdict(bool)
        with open(self.placePath, newline='') as csvfile:
            ratingReader = csv.reader(csvfile)
            next(ratingReader)
            for row in ratingReader:
                userID = int(row[0])
                smoker= bool(row[2])
                Smokers[userID]= bool(smoker)
        return Smokers
    
    def getArea(self):
        
        areas = defaultdict(str)
        with open(self.placePath, newline='') as csvfile:
            ratingReader = csv.reader(csvfile)
            next(ratingReader)
            for row in ratingReader:
                placeID = int(row[1])
                area= str(row[14])
                areas[placeID]= str(area)
        return areas
    
    def getRestaurantName(self, RestaurantID):
        if RestaurantID in self.placeID_to_name:
            return self.placeID_to_name[RestaurantID]
        else:
            return ""
        
    def getRestaurantID(self, RestaurantName):
        if RestaurantName in self.name_to_placeID:
            return self.name_to_placeID[RestaurantName]
        else:
            return 0    
        
    def getRestaurantType(self):
        infos = defaultdict(list)
        infosIDs = {}
        maxInfoID = 0
        with open(self.TestPath, newline='', encoding='ISO-8859-1') as csvfile:
            revReader = csv.reader(csvfile)
            next(revReader)  #Skip header line
            for row in revReader:
                restID = int(row[1])
                infoList = row[20].split('|')
                infoIDList = []
                for info in infoList:
                    if info in infosIDs:
                        infoID = infosIDs[info]
                    else:
                        infoID = maxInfoID
                        infosIDs[info] = infoID
                        maxInfoID += 1
                    infoIDList.append(infoID)
                infos[restID] = infoIDList
        # Convert integer-encoded genre lists to bitfields that we can treat as vectors
        for (restID, infoIDList) in infos.items():
            bitfield = [0] * maxInfoID
            for infoID in infoIDList:
                bitfield[infoID] = 1
            infos[restID] = bitfield            
        
        return infos
    
    
    
    
    def getUserType(self):
        infos = defaultdict(list)
        infosIDs = {}
        maxInfoID = 0
        with open(self.TestPath, newline='', encoding='ISO-8859-1') as csvfile:
            revReader = csv.reader(csvfile)
            next(revReader)  #Skip header line
            for row in revReader:
                userID = int(row[0])
                infoList = row[21].split('|')
                infoIDList = []
                for info in infoList:
                    if info in infosIDs:
                        infoID = infosIDs[info]
                    else:
                        infoID = maxInfoID
                        infosIDs[info] = infoID
                        maxInfoID += 1
                    infoIDList.append(infoID)
                infos[userID] = infoIDList
        # Convert integer-encoded genre lists to bitfields that we can treat as vectors
        for (userID, infoIDList) in infos.items():
            bitfield = [0] * maxInfoID
            for infoID in infoIDList:
                bitfield[infoID] = 1
            infos[userID] = bitfield            
        
        return infos