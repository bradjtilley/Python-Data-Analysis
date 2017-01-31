# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 22:27:41 2017

@author: hina
"""
# This file creates a basic user-based recommendation system for a sample
# user/music album/user rating nested dictionary. This code will find the 
# nearest neighbor for a specified user and recommend that user new albums
# which they have not rated yet. 

print ()

import math
from operator import itemgetter

# definie class similarity
class similarity:
    
    # Class instantiation 
    def __init__ (self, ratingP, ratingQ):
        self.ratings1 = ratingP
        self.ratings2 = ratingQ

    # Minkowski Distance between two vectors
    def minkowksi(self, r):
    
        # calcualte minkowski distance
        distance = 0       
        for k in (set(self.ratings1.keys()) & set(self.ratings2.keys())):
            p = self.ratings1[k]
            q = self.ratings2[k]
            distance += pow(abs(p - q), r)
    
        # return value of minkowski distance
        return pow(distance,1/r)

    # Pearson Correlation between two vectors
    def pearson(self):
        
        sumpq = 0
        sump = 0
        sumq = 0
        sump2 = 0
        sumq2 = 0
        n = 0

        # calcualte pearson correlation using the computationally efficient form        
        for k in (set(self.ratings1.keys()) & set(self.ratings2.keys())):
            n += 1
            p = self.ratings1[k]
            q = self.ratings2[k]
            sumpq += p * q
            sump += p
            sumq += q
            sump2 += pow(p, 2)
            sumq2 += pow(q, 2)
    
        # error check for n==0 condition
        if n == 0:
            print (">>> pearson debug: n=0; returning -2 correlation!")
            return -2    

        # calcualte nr and dr for pearson correlation
        nr = (sumpq - (sump * sumq) / n)
        dr = (math.sqrt(sump2 - pow(sump, 2) / n) * 
                        math.sqrt(sumq2 - pow(sumq, 2) / n))
        
        # error check for dr==0 condition
        if dr == 0:
            print (">>> pearson debug: denominator=0; returning -2 correlation!")
            return -2

        # return value of pearson correlation coefficient        
        return nr / dr

# user ratings
songData3 = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }

# for whom are we making recommendations?
userX = "Hailey"
userXRatings = songData3[userX]

# find the euclidean distance between userX's ratings, and each of the other user's ratings.
# use a for loop to get at the other users and their ratings
# use the similarity class to caclulate the euclidean distance between user ratings.

userDistances = []

for i in songData3:
    if i != userX:
        sds = similarity(userXRatings, songData3[i])
        dist = round(sds.minkowksi(2), 2)
        user_dist = i, dist
        userDistances.append(user_dist)
print(userDistances)

# sort list of tuples by lowest distance to highest distance.
userSortedDistances = []

from operator import itemgetter

userSortedDistances = sorted(userDistances, key = itemgetter(1))
print(userSortedDistances)

# userX's NN is the user at the 0th position of the sorted list.
userXNN = ""

userXNN = userSortedDistances[0][0]
print(userXNN)

# recos for userX will include albums rated by userXNN, not already rated by userX.
userXRecos = []

userXNND = songData3[userXNN]

for i in set(userXNND.keys()) - set(userXRatings.keys()):
    reco_list = i, userXNND[i]
    userXRecos.append(reco_list)
print(userXRecos)

# sort list of tuples by highest rating to lowest rating.
userXSortedRecos = []

from operator import itemgetter

userXSortedRecos = sorted(userXRecos, key = itemgetter(1), reverse=True)
print(userXSortedRecos)

print ("Recommendations for", userX)
print ("--------------------------")
print ()
print (userXSortedRecos)