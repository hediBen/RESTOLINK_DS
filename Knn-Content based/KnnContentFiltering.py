# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 13:08:53 2019

@author: hedi
"""

# -*- coding: utf-8 -*-


from surprise import AlgoBase
from surprise import PredictionImpossible
from ReviewsHandeling import Reviews
import math
import numpy as np
import csv
import heapq


class KnnContentFiltering(AlgoBase):
    
    
    DistRes ='C:\\Users\\hedi\\Desktop\\Graduation project\\Project\\ResDistances.csv'

    def __init__(self, k=40, sim_options={}):
        AlgoBase.__init__(self)
        self.k = k

    def fit(self, trainset):
        AlgoBase.fit(self, trainset)

        # Compute item similarity matrix based on content attributes

        # Load up genre vectors for every movie
        ml = Reviews ()
        typeR = ml.getRestaurantType()
        
        
        
        print("Computing content-based similarity matrix...")
            
        # Compute genre distance for every movie combination as a 2x2 matrix
        self.similarities = np.zeros((self.trainset.n_items, self.trainset.n_items))
        
        for thisRating in range(self.trainset.n_items):
            if (thisRating % 50 == 0):
                print(thisRating, " of ", self.trainset.n_items)
            for otherRating in range(thisRating+1, self.trainset.n_items):
                thisplaceID = int(self.trainset.to_raw_iid(thisRating))
                otherplaceID = int(self.trainset.to_raw_iid(otherRating))
                typeSimilarity = self.computeTypeSimilarity(thisplaceID, otherplaceID, typeR)
                distancesSimilarity = self.computeDistanceSimilarity(thisplaceID, otherplaceID)
                #mesSimilarity = self.computeMiseEnSceneSimilarity(thisMovieID, otherMovieID, mes)
                self.similarities[thisRating, otherRating] = typeSimilarity * distancesSimilarity
                self.similarities[otherRating, thisRating] = self.similarities[thisRating, otherRating]
                
        print("...done.")
                
        return self
    
    def computeTypeSimilarity(self, place1, place2, typeR):
        typeR1 = typeR[place1]
        typeR2 = typeR[place2]
        sumxx, sumxy, sumyy = 0, 0, 0
        for i in range(len(typeR1)):
            x = typeR1[i]
            y = typeR2[i]
            sumxx += x * x
            sumyy += y * y
            sumxy += x * y
        
        return sumxy/math.sqrt(sumxx*sumyy)
    

    def computeDistanceSimilarity(self,place1,place2):
        with open(self.DistRes, newline='') as csvfile:
            ratingReader = csv.reader(csvfile)
            next(ratingReader)
            for row in ratingReader:
                placex=int(row[0])
                placey=int(row[3])
                if ((place1 == placex) and (place2 == placey)):
                    dist = float(row[6])
                    sim = math.exp(-dist / 15.0)                 
        return sim    
#    
   

    def estimate(self, u, i):

        if not (self.trainset.knows_user(u) and self.trainset.knows_item(i)):
            raise PredictionImpossible('User and/or item is unkown.')
        
        # Build up similarity scores between this item and everything the user rated
        neighbors = []
        for rating in self.trainset.ur[u]:
            dessSimilarity = self.similarities[i,rating[0]]
            neighbors.append( (dessSimilarity, rating[1]) )
        
        # Extract the top-K most-similar ratings
        k_neighbors = heapq.nlargest(self.k, neighbors, key=lambda t: t[0])
        
        # Compute average sim score of K neighbors weighted by user ratings
        simTotal = weightedSum = 0
        for (simScore, rating) in k_neighbors:
            if (simScore > 0):
                simTotal += simScore
                weightedSum += simScore * rating
            
        if (simTotal == 0):
            raise PredictionImpossible('No neighbors')

        predictedRating = weightedSum / simTotal

        return predictedRating
    
        