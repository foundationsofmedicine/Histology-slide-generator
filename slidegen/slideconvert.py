import os
from slidegen import fileio as io

def convertall(loc, saveloc):
    filels = os.listdir(loc)
    for i in range(len(filels)):
        file = filels[i].split(".")[0]
        if int(file) < 7740: # because i stopped at 7740
            continue
        else:
            converttojpg(file, loc, saveloc)
    return
    # Stopped at 7740

def converttojpg(slide_ID, loc, saveloc):
    # print("vips openslideload --level 0 " + loc + slide_ID + ".svs '" + saveloc + slide_ID + ".jpg'")
    os.system("vips openslideload --level 0 " + loc + slide_ID + ".svs '" + saveloc + slide_ID + ".jpg'")
    return

def generateDZIs(slideList, src, dest):
    filels = os.listdir(src)
    for i in range(len(filels)):
        file = int(filels[i].split(".")[0])
        # print(file)
        slide_data = slideList[slideList['slide_filename'] == file]
        # print(slide_data)
        slide_ID = slide_data['slide_ID'].values[0]
        converttodzi(file, src, slide_ID, dest)
    return

def converttodzi(slide_id, loc, destfilename, dest):
    io.generateFolder("./public/" + destfilename)
    # print("vips dzsave '" + loc + str(slide_id) + ".jpg' " + dest + destfilename + "/slide")
    os.system("vips dzsave '" + loc + str(slide_id) + ".jpg' " + dest + destfilename + "/slide")
    return

# print(slideList)
# slidename = 7700
# slideRow = slideList[slideList['slide_filename'] == slidename]
# print(slideRow['slide_ID'].values[0])