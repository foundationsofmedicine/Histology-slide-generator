import os
import pandas as pd
import shutil


def generateFolder(loc):
    if not os.path.exists(loc):
        os.mkdir(loc)
        print("Made folder " + loc)

def readSlideList(loc):
    slideList = pd.read_csv(loc)
    """ Note that the Slide List CSV should have the following headings:
            - slide_ID
            - slide_name
        Additionally, the Slide_ID should have the same name (with exception of the file extension) as the actual slide file
    """
    slide_IDs = slideList['slide_ID'].tolist()
    return slideList, slide_IDs

def copyTree(from_path, to_path):
    if os.path.exists(to_path):
        shutil.rmtree(to_path)
    shutil.copytree(from_path, to_path)