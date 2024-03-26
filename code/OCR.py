#%%
import pytesseract
from PIL import Image
import pdf2image
#%%
# Set the path for the Tesseract engine executable
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
# pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
# pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\amjad\\Downloads\\poppler-24.03.0.tar\\poppler-24.03.0'
# Convert the first page of PDF to an image
poppler_path = r'C:\\Users\\amjad\\Downloads\\poppler-24.02.0\\library\\bin'
def convert_pdf_to_image(pdf_path):
    return pdf2image.convert_from_path(pdf_path, poppler_path=poppler_path) # specified the path for poppler

# Perform OCR on the images
def ocr_images(images):
    all_text = []
    for img in images:
        text = pytesseract.image_to_string(img, lang='eng')  # 'eng' for English
        if 'Table 4' in text:  # Check if 'Table 4' is in the OCR'd text
            all_text.append(text)  # If so, add the text to our list
    return all_text

# Path to the PDF file
pdf_path = '../data/2012.pdf'
#%%
# Convert PDF to images
images = convert_pdf_to_image(pdf_path)

#%%
# Extract text from the images using OCR
extracted_texts = ocr_images(images)

# The OCR process is done, let's see the first 1000 characters of the extracted text
print(extracted_texts[0][:10000])  


# %%
names =['General Index', 
'FOOD AND BEVERAGES', 
'FOOD',
'BEVERAGES ',
'TOBACCO ',
'TOBACCO', 
'CLOTHING AND FOOTWEAR',
'CLOTHING',
'FOOTWEAR',
'HOUSING, WATER, ELECTRI-CITY',
'GAS AND OTHER FUELS GAY',
'RENTALS FOR HOUSING',
'MAITENANCE OF THE DEWELLING',
'WATER SUPPLY & OTHER SERVICES', 
'ELECTRICITY, GAS AND OTHER FUELS', 
'FURNISHINGS, HOUSEHOLD', 
'EQUIPMENT AND MAINTENANCE',
'FURNITURE & CARPETS.', 
'HOUSEHOLD TEXTILES',
'HOUSEHOLD APPLIANCES', 
'HOUSEHOLD UTENSILS',
'TOOLS FOR HOUSE & GARDEN',
'GOODS FOR HOUSEHOLD',
'MAINTENANCE',
'HEALTH',
'MEDICAL PRODUCTS & EQUIPMENT', 
'OUTPATIENT SERVICES',
'HOSPITAL SERVICES', 
'TRANSPORT',
'PURCHASE OF VEHICLES', 
'OPERATION OF TRANSPORT',
'EQUIPMENT',
'TRANSPORT SERVICES', 
'COMMUNICATION',
'POSTAL SERVICES',
'TELEPHONE AND TELEFAX EQUIPMENT',
'TELEPHONE AND TELEFAX SERVICES',
'RECREATION AND CULTURE',
'AUDIO, PHOTO & INFO. EQUIPMENT',
'OTHER RECREATION & CULTURE GOODS',
'OTHER RECREATIONAL GOODS',
'RECREATIONAL & CULTURAL SERVICES',
'NEWSPAPERS, BOOKS & STATIONERY',
'PACKAGE HOLIDAYS',
'EDUCATION',
'PRE-PRIMARY & PRIMARY EDUCATION',
'SECONDARY&INTERMEDIATE EDUCATION',
'POST-SECONDARY EDUCATION',
'TERTIARY EDUCATION',
'RESTAURANTS AND HOTELS',
'CATERING SERVICE',
'ACCOMMODATION SERVICES',
'MISCELLANEOUS GOODS AND SERVICES',
'PERSONAL CARE',
'PERSONAL EFFECTS N.E.C.',
'SOCIAL PROTECTION',
'INSURANCE',''
'FINANCIAL SERVICES N.E C.',
'OTHER SERVICES N.E'] # check the names in the rows coz not all of them in the same line

# %%
