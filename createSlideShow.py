from slide import Slide
from Photo import Photo
import math
import operator

#This function takes a list of slides, and compares the feature vectors
#to create an ordered slideshow
def createSlideShow(vocabulary,slides):
    vectors = [(slide.vector(vocabulary),slide) for slide in slides]

    bestMatch = vectors.pop(0)
    slideShow = [bestMatch[1]]
    while True:
        listOfBest = [(euclideanDistance(bestMatch[0],v),s) for v,s in vectors]
        listOfBest.sort(key = operator.itemgetter(0))
        print(listOfBest)
        median = math.floor(len(listOfBest)/2)
        slideShow.append(listOfBest[median][1])
        bestMatch = listOfBest[median][1]
        vectors.pop(vectors.index(bestMatch))
        break


    
def euclideanDistance(v1,v2):
    thing = 0
    for i in range(len(v1)):
        thing += (v1[i] - v2[i])**2
    return math.sqrt(thing)

p1 = Photo(1,"H",2,["cat"])
p2 = Photo(2,"H",2,["sunny","person"])
p3 = Photo(3,"H",2,["cat","person"])
p4 = Photo(4,"H",3,["sunny","cat","person"])
p5 = Photo(5,"H",0,[])
createSlideShow(["cat","sunny","person"], [p1,p2,p3,p4,p5])

            #listOfBest.sort(key = operator.itemgetter(0))

