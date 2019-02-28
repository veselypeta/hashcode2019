from Photo import Photo

def parseData(filename):
    with open(filename, 'r') as inputFile:
        lines = inputFile.readlines()
        lines = [x[0:-1] for x in lines]
        n = int(lines[0])
        photos = []
        for i in range(1,n):
            photo = lines[i].split(' ')
            orientation = photo[0]
            n_tags = int(photo[1])
            tags = []
            for j in range(2, n_tags+2):
                tags.append(photo[j])
            p = Photo(i, orientation, n_tags, tags)
            photos.append(p)
    
    return photos

def vocabulary(photos):
    vocabulary = []
    for photo in photos:
        for tag in photo.tags_list:
            if tag not in vocabulary:
                vocabulary.append(tag)
    return vocabulary


ps = parseData("a_example.txt")
for p in ps:
    print(p.tags_list)
v = vocabulary(ps)
print(v)
