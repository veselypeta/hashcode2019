
# A slide contains a list of photos. The list can either contain one horizontal
# Or two vertical photos, and also stores a list of their combined tags
class Slide():
    def __init__(self,photo1,photo2):
        self.left_photo = photo1
        self.right_photo = photo2
        self.tags = self.left_photo.tags_list
        for t in self.right_photo.tags_list:
            if t not in self.tags:
                self.tags.append(t)

def create_vertical_slides(verticals):
    v_front = []
    v_back = []
    for i in range(len(verticals)):
        for j in range(i, len(verticals)):
            s = Slide(verticals[i], verticals[j])
            v_slides.append(s) 
    return v_slides

