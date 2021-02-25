from slidegen import fileio as io
from slidegen import generatePages as gp
from slidegen import slideconvert as sc


# io.generateFolder("./public")
slideList, slide_IDs = io.readSlideList("./src/slides.csv")

'''CONVERT ALL THE SLIDES FIRST BEFORE STARTING '''
# sc.convertall("/Volumes/SSD/2021-02-15/", "/Volumes/Webers SSD/Projects/UsydPathSlides/")
# Keep note of which slides you were unable to generate JPEGs for - may need a different approach (i.e. issue if max dimension > 65500px)
# Unable to convert 7698 and 7696
sc.generateDZIs(slideList, "/Volumes/Webers SSD/Projects/UsydPathSlides/", "./public/")
'''CONVERSION COMPLETE, COPY FILES OVER'''



# gp.generateSlides(slideList, "./public")
# gp.generateLanding(slideList, "./public")

#Copy OSD files to the public directory
# io.copyTree("./src/openseadragon-bin-2.4.1", "./public/openseadragon-bin-2.4.1")



# io.copyTree("./public", "../foundationsofmedicine.github.io/basicscience/usydpath")