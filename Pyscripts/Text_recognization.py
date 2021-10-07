import easyocr
import isbnlib
from isbntools.app import *

def image(img):
    reader = easyocr.Reader(['en'])
    output = reader.readtext(img)
    final_text=""
    for i in range(0,len(output)):
        text=output[i][1]
        final_text=final_text +" "+ text
    get_isbn = isbn_from_words(final_text)
    dict={}
    dict=isbnlib.meta(str(get_isbn))
    return dict
