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
    # Here we convert only the first page
    return pdf2image.convert_from_path(pdf_path, first_page=0, last_page=1, poppler_path=poppler_path) # specified the path for poppler

# Perform OCR on the images
def ocr_images(images):
    all_text = []
    for img in images:
        text = pytesseract.image_to_string(img, lang='eng')  # 'eng' for English, use different language codes as needed
        all_text.append(text)
    return all_text

# Path to the PDF file
pdf_path = '../data/2014.pdf'
#%%
# Convert PDF to images
images = convert_pdf_to_image(pdf_path)
#%%
# Extract text from the images using OCR
extracted_texts = ocr_images(images)

# The OCR process is done, let's see the first 1000 characters of the extracted text
print(extracted_texts[0][:10000])  # Print only the first 1000 characters to avoid too long output



# %%
