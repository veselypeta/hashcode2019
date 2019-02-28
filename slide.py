
#This class takes a list of photos which will have length one or two
#And stored them as well as their combined tags
class Slide():
    def __init__(self,photos):
        self.photos = photos # two photos
        self.tags = []
        self.tags.append(photos[0].tags)
        if len(photos) == 2:
            self.tags.append(photos[1].tags)

        self.n_tags = len(self.tags) 

                      


def create_vertical_slides(verticals):
    v_slides = []
    for i in range(len(verticals)):
        for j in range(i, len(verticals)):
            s = Slide([verticals[i],verticals[j]])
            v_slides.append(s) 
    return v_slides

