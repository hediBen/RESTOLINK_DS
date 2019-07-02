# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 13:57:55 2019

@author: hedi
"""

# -*- coding: utf-8 -*-


from KnnContentFiltering import KnnContentFiltering
from Evaluator import Evaluator
from surprise import NormalPredictor
from ReviewsHandeling import Reviews
import numpy as np


def LoadRevsData():
    ml = Reviews()
    print("Loading restaurant ratings...")
    data = ml.loadRevDataSet()
    print("\nComputing restaurant popularity ranks so we can measure novelty later...")
    rankings = ml.getPopularityRanks()
    return (ml, data, rankings)

np.random.seed(0)


# Load up common data set for the recommender algorithms
(ml, evaluationData, rankings) = LoadRevsData()

# Construct an Evaluator to, you know, evaluate them
evaluator = Evaluator(evaluationData, rankings)

contentKNN = KnnContentFiltering()
evaluator.AddAlgorithm(contentKNN, "ContentKNN")

# Just make random recommendations
Random = NormalPredictor()
evaluator.AddAlgorithm(Random, "Random")

evaluator.Evaluate(False)

evaluator.SampleTopNRecs(ml)
