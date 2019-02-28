from slide import *
from parse import *


def output_file(slideshow):
    with open("we_are_the_champions.txt", 'w') as myFile:
        n = len(slideshow)
        myFile.write(str(n) + "\n")
            

photos = parseData("d_pet_pictures.txt")
verticals = [x for x in photos if x.orientation=='V']
horizontals = [x for x in photos if x.orientation=='H']
verticalSlides = create_vertical_slides(verticals)

all_photos = horizontals + verticalSlides

print(len(all_photos))