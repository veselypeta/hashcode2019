
#This class takes a list of photos which will have length one or two
#And stored them as well as their combined tags
class Slide():
    def __init__(self,photos):
        self.photos = photos
        self.tags = []
        self.tags.append(photos[0].tags)
        if len(photos) == 2:
            self.tags.append(photos[1].tags)            
