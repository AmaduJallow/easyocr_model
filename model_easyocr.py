import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import easyocr
import cv2
import numpy as np
import matplotlib.pyplot as matplotlib


def image_to_text(image_url):
    bytedata = bytes(image_url, "UTF-8")
    reader = easyocr.Reader(['en'], gpu=True)
    result = reader.readtext(bytedata.decode())
    value = ""
    for data in result:
        for line in data:
            if type(line) == str:
                value += " " + line
    return value
