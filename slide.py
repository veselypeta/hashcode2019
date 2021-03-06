from math import floor, ceil
# A slide contains a list of photos. The list can either contain one horizontal
# Or two vertical photos, and also stores a list of their combined tags
class Vertical_Photo():
    def __init__(self,photo1,photo2):
        self.left_photo = photo1
        self.right_photo = photo2
        self.tags_list = self.left_photo.tags_list
        for t in self.right_photo.tags_list:
            if t not in self.tags_list:
                self.tags_list.append(t)
    
    def vector(self, vocabulary):
        vector = [0] * len(vocabulary)
        for i, tag in enumerate(vocabulary):
            if tag in self.tags_list:
                vector[i] = 1
        return vector
    
def create_vertical_slides(verticals):
    marker = floor(len(verticals)/2)
    front = verticals[0:marker]
    back = verticals[marker+1 ::]
    back = list(reversed(back))
    pairs = zip(front, back)
    slides = []
    for x, y in pairs:
        s = Vertical_Photo(x, y)
        slides.append(s)
    return slides


