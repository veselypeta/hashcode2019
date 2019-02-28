from slide import *
from parse import *

photos = parseData("d_pet_pictures.txt")
verticals = [x for x in photos if x.orientation=='V']
verticalSlides = create_vertical_slides(verticals)
print(len(verticalSlides))