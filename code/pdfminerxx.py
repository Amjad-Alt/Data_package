# %%
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams
from io import StringIO
import os
import pandas as pd
import re

# %%
# pdf_path = "/Users/amjad/OneDrive/المستندات/GWU_Cources/Spring2024/capstone_project/data/2002.pdf"

# def convert_pdf_to_html(pdf_path):
#     output = StringIO()
#     with open(pdf_path, 'rb') as pdf_file:
#         extract_text_to_fp(pdf_file, output, laparams=LAParams(),
#                            output_type='html', codec=None)
#     html_content = output.getvalue()
#     return html_content


# # Example usage
# # pdf_path = 'example.pdf'  # Replace 'example.pdf' with your PDF file path
# html_content = convert_pdf_to_html(pdf_path)

# # To save the HTML content to a file
# html_file_path = 'output.html'  # Output HTML file path
# with open(html_file_path, 'w', encoding='utf-8') as html_file:
#     html_file.write(html_content)

# print(f"PDF has been converted to HTML and saved as {html_file_path}")

#%%
# pull information from html file
# selector for city 
# body > div:nth-child(13520) > span

import pdfplumber

def extract_first_column(pdf_path):
    yoffset = 190
    xoffset = 0
    all_text_lines = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            yheight = page.height - yoffset
            xwidth = page.width *0.4
            # Define the bounding box (crop box) for the first column
            # This example assumes the first column is within the left half of the page.
            # You may need to adjust these coordinates based on the actual layout of your PDF.
            # The bounding_box is in the format (x0, top, x1, bottom), with:
            # x0: the left edge of the column
            # top: the top edge of the column (usually 0 to start from the top)
            # x1: the right edge of the column
            # bottom: the bottom edge of the column (use page.height to cover until the bottom of the page)
            bounding_box = (xoffset, yoffset, xwidth, yheight)
            
            # Crop the page to the bounding box to focus on the first column
            cropped_page = page.within_bbox(bounding_box)
            
            # Extract text from the cropped area
            text = cropped_page.extract_text()
            
            if text:
                # Split the text into lines and add them to the list
                all_text_lines.extend(text.split('\n'))

    return all_text_lines

# Example usage
pdf_path = "/Users/amjad/OneDrive/المستندات/GWU_Cources/Spring2024/capstone_project/data/2003_sample.pdf"

# pdf_path = 'example.pdf'  # Replace 'example.pdf' with your PDF file path
data = extract_first_column(pdf_path)


# %%


# Process each line to separate text and numbers
processed_data = []
for line in data:
    # Find all number groups in the line
    numbers = re.findall(r"\d+\.\d+|\d+", line)
    # Find the text part by replacing numbers with an empty string
    text = re.sub(r"\d+\.\d+|\d+", '', line).strip()
    # Combine text and numbers into a list, with text as the first element
    row = [text] + numbers
    processed_data.append(row)

# Convert the list of lists into a DataFrame
df = pd.DataFrame(processed_data)

# Optionally, rename columns for clarity
column_names = ['Category'] + [f'Value {i+1}' for i in range(df.shape[1]-1)]
df.columns = column_names

# Display the DataFrame
print(df)

#%%


def extract_first_column(pdf_path):
    yoffset = 0
    xoffset = 0
    all_text_lines = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            yheight = page.height - yoffset
            xwidth = page.width *0.4
            # Define the bounding box (crop box) for the first column
            # This example assumes the first column is within the left half of the page.
            # You may need to adjust these coordinates based on the actual layout of your PDF.
            # The bounding_box is in the format (x0, top, x1, bottom), with:
            # x0: the left edge of the column
            # top: the top edge of the column (usually 0 to start from the top)
            # x1: the right edge of the column
            # bottom: the bottom edge of the column (use page.height to cover until the bottom of the page)
            bounding_box = (xoffset, yoffset, xwidth, yheight)
            
            # Crop the page to the bounding box to focus on the first column
            cropped_page = page.within_bbox(bounding_box)
            
            # Extract text from the cropped area
            text = cropped_page.extract_text()
            
            if text:
                # Split the text into lines and add them to the list
                all_text_lines.extend(text.split('\n'))

    return all_text_lines

data2 = extract_first_column(pdf_path)