from jinja2 import Environment, select_autoescape
from jinja2.loaders import FileSystemLoader
import pandas as pd

env = Environment(
    loader=FileSystemLoader('./src/templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

def savePage(htmlObj, location):
    with open(location, "w") as f:
        f.write(htmlObj)

def generateSlides(slideList, loc):

    page = env.get_template("slide_template.html")
    htmlObj = page.render()
    savePage(htmlObj, "./public/" +  + "/index.html")
    return

def generateLanding(slideList, loc):

    page = env.get_template("landing_template.html")
    htmlObj = page.render()
    savePage(htmlObj, "./public/index.html")
    return