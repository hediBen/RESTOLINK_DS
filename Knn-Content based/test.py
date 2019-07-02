# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 14:59:58 2019

@author: hedi
"""
from ReviewsHandeling import Reviews
from KnnContentFiltering import KnnContentFiltering
from EvaluationData import EvaluationData
ml = Reviews()

data = ml.loadRevDataSet()
   
rankings = ml.getPopularityRanks()


tt=EvaluationData(data, rankings)
tt.GetTrainSet()