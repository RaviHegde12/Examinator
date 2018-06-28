import os
import pytesseract
from examinator.settings.common import MEDIA_ROOT
from PIL import Image, ImageEnhance, ImageFilter


def ImageToTextConverter(file):
    path = MEDIA_ROOT +"/images/"+ file
    img = Image.open(path)
    img = img.convert('RGB')
    pix = img.load()
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if pix[x, y][0] < 102 or pix[x, y][1] < 102 or pix[x, y][2] < 102:
                pix[x, y] = (0, 0, 0, 255)
            else:
                pix[x, y] = (255, 255, 255, 255)
    img.save(MEDIA_ROOT+'/images/processed_' + file)
    text = pytesseract.image_to_string(Image.open(MEDIA_ROOT+'/images/processed_' + file))
    os.remove(MEDIA_ROOT+'/images/processed_' + file)
    text_ouput = open(MEDIA_ROOT+"/images/text_" + file + ".txt", "w")
    text_ouput.write(text)
    text_ouput.close()
    return text
