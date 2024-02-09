
import fitz 
import pandas as pd
import re

def extract_text_from_pdf(pdf_path, page_numbers):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in page_numbers:
        # Check if the page number is valid
        if page_num < len(doc):
            text += doc[page_num].get_text()
    return text

pages_to_extract = [10, 11,12, 13, 14, 15, 16, 17] 

def parse_text_to_data(text):
    # Delete non-English characters
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s,.]', '', text)
    # Split the cleaned text into lines or comma-separated values
    elements = re.split(r'[\n,]+', cleaned_text.strip())
    # Filter out empty elements and elements containing only periods (with flexible length)
    filtered_elements = [element for element in elements if element and not re.fullmatch(r'\.+', element.strip())]
    # Group filtered elements into rows with 7 elements each
    rows = [filtered_elements[i:i+7] for i in range(0, len(filtered_elements), 7)]
    return rows


def create_csv_from_data(data, csv_path):
    df = pd.DataFrame(data[1:], columns=data[0]) 
    df.to_csv(csv_path, index=False)

pdf_path = '/Users/amjad/OneDrive/المستندات/GWU_Cources/Spring2024/capstone_project/data/2002.pdf'  # Update with the path to your PDF
csv_path = '/Users/amjad/OneDrive/المستندات/GWU_Cources/Spring2024/capstone_project/code/output.csv'  # Update with your desired CSV path

text = extract_text_from_pdf(pdf_path,pages_to_extract)
print(text)
data = parse_text_to_data(text)

create_csv_from_data(data, csv_path)


