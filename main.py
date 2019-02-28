from slide import *
from parse import *
from Photo import *
from createSlideShow import *
from orientation import *

def output_file(slideshow):
    with open("we_are_the_champions.txt", 'w') as myFile:
        n = len(slideshow)
        myFile.write(str(n) + "\n")
        for slide in slideshow:
            if isinstance(slide, Vertical_Photo):
                myFile.write(str(slide.left_photo.photo_id) + " " + str(slide.right_photo.photo_id) + "\n")
            if isinstance(slide, Photo):
                myFile.write(str(slide.photo_id) + "\n")


photos = parseData("b_lovely_landscapes.txt")
verticals = [x for x in photos if x.orientation=='V']
horizontals = [x for x in photos if x.orientation=='H']
verticalSlides = create_vertical_slides(sortList(verticals))
print("verticalSlides done")

all_photos = horizontals + verticalSlides
print("allphotos done")
vocab = vocabulary(photos)
print("creatingshow")

s = createSlideShow(vocab, all_photos)
output_file(s) 
