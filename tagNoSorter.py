from slide import Slide

#Takes a list of slides and returns a list of list based on the size of tags
def tagNoSorter(slides):
    maxTagNo = 0
    for slide in slides:
        if len(slide.tags) > maxTagNo:
            maxTagNo = len(slide.tags)
    print(maxTagNo)

    tagNoList = []
    for tagNo in range(100000):
        if slides:
            tagNoList.append([slide for slide in slide])

s = Slide([])
