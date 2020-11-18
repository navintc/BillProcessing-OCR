#****I know this code can be shortned with regex functions, But I avoided them. Due to the fact that i dont understand them.*****

from PIL import Image
import pytesseract
import numpy as np

#no matter how intelligent you are, you still have to reference the
#tesseract binary file to make functional, even after pulling the tessearct
#library. I dont know what this is why should we do it but, you have to embed you tesseract (binary)
#installation path to "pytesseract.pytesseract.tesseract_cmd"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#import the image
filename = 'sliptxt.png'
#add it to a numpy array
img1 = np.array(Image.open(filename))
#let the tesseract do the scraping
text = pytesseract.image_to_string(img1)

#so machan, tesseract can give a clean peice of data even though the google is feeding it.
#therefore, you have to use split to remove aditional white spaces and give single spaces.
final = (' '.join(text.split()))

#clearing data
final = final.replace('|', ' ')
final = final.replace('/', ' ')
final = final.replace(')', ' ')
final = final.replace('.', '')
final = final.replace("'", ' ')
final = final.replace('_', '')
final = final.replace('-', '')
final = final.replace('}', '')
final = final.replace(':', '')






#TESTING-----------------------------------------------------------------------------------------------------------------
#scraping name by taking the data "beforeHospital", "afterHospital" and the "hospital" keyword itself

# bHospital, kHospital, aHospital = final.partition('Hospital')
# name = bHospital.replace('Name ', '')
                                                                                                                                                                                                                                                                                                                                                                                                                                             

#scrap hospital by substracting before hospital and  "hospital" from before ward

# bWard, kWard, aWard = final.partition('Ward')
# hospital = bWard.replace('Hospital ', '')
# hospital = hospital.replace(bHospital, '')

#Same shit for the ward

# bSpecialty, kSpecialty, aSpecialty = final.partition('Specialty')
# ward = bSpecialty.replace('Ward ', '')
# ward = ward.replace(bWard, '')
#TESTING-----------------------------------------------------------------------------------------------------------------

dataBoi = {}
partitionStrings = ['Name', 'Hospital', 'Ward', 'Specialty', 'Band', 'Date', 'Start', 'Finish', 'Break', 'Total Hours Worked', 'Reference', 'Induction Delivery', 'Client Shift Apprasial', 'AppName', 'ApName', 'ApSpecialty', 'Done']
replaceStrings = ['Name ','Hospital ', 'Ward ', 'Specialty ', 'Band ', 'Date', 'Start ', 'Finish ', 'Break ', 'Total Hours Worked ', 'Reference ', 'Induction Delivery ', 'Client Shift Apprasial ', 'AppName ', 'ApName ', 'ApSpecialty ', 'Done' ]

for i in range (len(partitionStrings)-1):
    bbw, kw, aw = final.partition(partitionStrings[i])
    bw, kw, aw = final.partition(partitionStrings[i+1])
    ward = bw.replace(replaceStrings[i], '')
    ward = ward.replace(bbw, '')
    dataBoi[partitionStrings[i]] = ward
    # print (ward)
print(dataBoi)
