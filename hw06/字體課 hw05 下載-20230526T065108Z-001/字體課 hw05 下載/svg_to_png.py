import os
import xml.etree.ElementTree as ET
import cairosvg
from cairosvg import svg2png
from nturl2path import url2pathname
from PIL import Image
from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg



allFileList = os.listdir("./svg")

def rgba_to_rgb(fileName):
    png = Image.open("./png_test/"+fileName).convert('RGBA')
  

    background = Image.new("RGBA", png.size, (255, 255, 255))
    alpha_composite = (Image.alpha_composite(background, png)).convert('RGB')

    alpha_composite = alpha_composite.resize((128, 128))
    alpha_composite.save('./png_portrace/'+'U+'+fileName[:-4] + '.png', 'PNG',quality=50)


    print('Success_to_rgb!')

for file in allFileList:
  cairosvg.svg2png(url="./svg/" + file, write_to='./png_test/' + file[2:-4] +'.png')
  rgba_to_rgb(file[2:-4] +'.png')
  print('Success!')

  