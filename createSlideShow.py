from slide import *
from Photo import Photo
import math
import operator

#This function takes a list of slides, and compares the feature vectors
#to create an ordered slideshow
def createSlideShow(vocabulary,slides):
    vectors = [(slide.vector(vocabulary),slide) for slide in slides]

    bestMatch = vectors.pop(0)
    slideShow = [bestMatch[1]]
    while len(vectors)>1:
        # get a list of distances to each point from the presious best result
        listOfBest = [(euclideanDistance(bestMatch[0],v),s) for v,s in vectors]
        
        # sort by the shortest distance
        listOfBest.sort(key = operator.itemgetter(0))
        # median location
        median = math.floor(len(listOfBest)/2)
        bestSlide = listOfBest[median][1]
        # add the photo to the slideshow
        bestMatch = [(a,b) for a, b in vectors if b == bestSlide][0]
        slideShow.append(bestMatch[1])
        # find the slide in vectors which corresponds to best slide
        vectors.pop(vectors.index(bestMatch))
    
    #slideShow.append(vectors[0][1])
    return slideShow


def euclideanDistance(v1,v2):
    thing = 0
    for i in range(len(v1)):
        thing += (v1[i] - v2[i])**2
    return math.sqrt(thing)

