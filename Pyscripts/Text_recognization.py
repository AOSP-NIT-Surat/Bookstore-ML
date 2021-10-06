#pip install easyocr

#pip install isbntools

import easyocr

from isbntools.app import *

reader = easyocr.Reader(['en'])
output = reader.readtext('test.jpg')
final_text=""
for i in range(0,len(output)):
    text=output[i][1]
    final_text=final_text +" "+ text
    #print(text)

#print(final_text)
get_isbn = isbn_from_words(final_text)



print(registry.bibformatters['labels'](meta(get_isbn)))