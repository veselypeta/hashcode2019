
# A slide contains a list of photos. The list can either contain one horizontal
# Or two vertical photos, and also stores a list of their combined tags
class Slide():
    def __init__(self,photo1,photo2=None):
        self.photos = [photo1]
        self.tags = [photo1.tags]
        if photo2 != None:
            self.photos.append(photo2)
            self.tags.append(photo2.tags)

        self.n_tags = len(self.tags) 

    def 
                      


def create_vertical_slides(verticals):
    for
