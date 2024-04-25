# %%
import pytesseract
from PIL import Image
import pdf2image
import os
import glob
import pandas as pd
import re
# %%
# # Set the path for the Tesseract engine executable
# pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# # pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
# # pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
# # pytesseract.pytesseract.tesseract_cmd = r'C:\\Users\\amjad\\Downloads\\poppler-24.03.0.tar\\poppler-24.03.0'
# # Convert the first page of PDF to an image
# poppler_path = r'C:\\Users\\amjad\\Downloads\\poppler-24.02.0\\library\\bin'
# def convert_pdf_to_image(pdf_path):
#     return pdf2image.convert_from_path(pdf_path, poppler_path=poppler_path) # specified the path for poppler

# # Perform OCR on the images
# def ocr_images(images):
#     all_text = []
#     for img in images:
#         text = pytesseract.image_to_string(img, lang='eng')  # 'eng' for English
#         if 'Table 4' in text:  # Check if 'Table 4' is in the OCR'd text
#             all_text.append(text)  # If so, add the text to our list
#     return all_text

# # Path to the PDF file
# pdf_path = '../data/2012.pdf'
# #%%
# # Convert PDF to images
# images = convert_pdf_to_image(pdf_path)

# #%%
# # Extract text from the images using OCR
# extracted_texts = ocr_images(images)

# # The OCR process is done, let's see the first 1000 characters of the extracted text
# print(extracted_texts[0][:10000])


# # %%
# names =['General Index',
# 'FOOD AND BEVERAGES',
# 'FOOD',
# 'BEVERAGES ',
# 'TOBACCO ',
# 'TOBACCO',
# 'CLOTHING AND FOOTWEAR',
# 'CLOTHING',
# 'FOOTWEAR',
# 'HOUSING, WATER, ELECTRI-CITY',
# 'GAS AND OTHER FUELS GAY',
# 'RENTALS FOR HOUSING',
# 'MAITENANCE OF THE DEWELLING',
# 'WATER SUPPLY & OTHER SERVICES',
# 'ELECTRICITY, GAS AND OTHER FUELS',
# 'FURNISHINGS, HOUSEHOLD',
# 'EQUIPMENT AND MAINTENANCE',
# 'FURNITURE & CARPETS.',
# 'HOUSEHOLD TEXTILES',
# 'HOUSEHOLD APPLIANCES',
# 'HOUSEHOLD UTENSILS',
# 'TOOLS FOR HOUSE & GARDEN',
# 'GOODS FOR HOUSEHOLD',
# 'MAINTENANCE',
# 'HEALTH',
# 'MEDICAL PRODUCTS & EQUIPMENT',
# 'OUTPATIENT SERVICES',
# 'HOSPITAL SERVICES',
# 'TRANSPORT',
# 'PURCHASE OF VEHICLES',
# 'OPERATION OF TRANSPORT',
# 'EQUIPMENT',
# 'TRANSPORT SERVICES',
# 'COMMUNICATION',
# 'POSTAL SERVICES',
# 'TELEPHONE AND TELEFAX EQUIPMENT',
# 'TELEPHONE AND TELEFAX SERVICES',
# 'RECREATION AND CULTURE',
# 'AUDIO, PHOTO & INFO. EQUIPMENT',
# 'OTHER RECREATION & CULTURE GOODS',
# 'OTHER RECREATIONAL GOODS',
# 'RECREATIONAL & CULTURAL SERVICES',
# 'NEWSPAPERS, BOOKS & STATIONERY',
# 'PACKAGE HOLIDAYS',
# 'EDUCATION',
# 'PRE-PRIMARY & PRIMARY EDUCATION',
# 'SECONDARY&INTERMEDIATE EDUCATION',
# 'POST-SECONDARY EDUCATION',
# 'TERTIARY EDUCATION',
# 'RESTAURANTS AND HOTELS',
# 'CATERING SERVICE',
# 'ACCOMMODATION SERVICES',
# 'MISCELLANEOUS GOODS AND SERVICES',
# 'PERSONAL CARE',
# 'PERSONAL EFFECTS N.E.C.',
# 'SOCIAL PROTECTION',
# 'INSURANCE',''
# 'FINANCIAL SERVICES N.E C.',
# 'OTHER SERVICES N.E'] # check the names in the rows coz not all of them in the same line

# %%
class OCRAAlt:
    """
    A class to extract data from PDF files, focusing on structured data extraction.
    When dealing with PDFs, it specifically looks for pages that contain "Table 4" using OCR.
    Then extract months, year, cities from each page.
    Then extract rowIndex with it's values.
    Then mach months, year, cities with their rowIndex and values.
    Then the output is data fram that has all the information 
    """

    def __init__(self, pdf_path=""):
        """
        Constructor initializes the class with lists of cities, months, years,
        and sets up a multi-index DataFrame for storing extracted data.
        """
        # self.cities = [
        #     "MAKKAH", "RIYADH", "TAIF", "JEDDAH", "BURAYDAH", "MEDINA",
        #     "ALHOFOF", "DAMMAM", "TABUK", "ABHA", "JAZAN", "HAIL", "BAHA",
        #     "NJRAN", "ARAR", "SKAKA"
        # ]
        self.cities = [
            "MAKKAH", "RIYADH", "TAIF", "JEDDAH", "BURAYDAH", "MEDINA",
            "ALHOFOF", "DAMMAM", "TABUK", "ABHA", "JAZAN", "HAIL", "BAHA",
            "NJRAN", "ARAR", "SKAKA"
        ]
        self.months = [
            "JAN", "FEB", "MAR", "APR", "MAY", "JUN",
            "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"
        ]
        self.years = list(range(2012, 2014))

        # Setup multi-level columns for the DataFrame
        multicolumns = pd.MultiIndex.from_product(
            [self.cities, self.years, self.months],
            names=['City', 'Year', 'Month']
        )

        self.rowIndices = ['General Index',
                           'FOOD AND BEVERAGES',
                           'FOOD',
                           'BEVERAGES',
                           'TOBACCO',
                           'CLOTHING AND FOOTWEAR',
                           'CLOTHING',
                           'FOOTWEAR',
                           'HOUSING, WATER, ELECTRI-CITY ,GAS AND OTHER FUELS',
                           'RENTALS FOR HOUSING',
                           'MAITENANCE OF THE DEWELLING',
                           'WATER SUPPLY & OTHER SERVICES',
                           'ELECTRICITY, GAS AND OTHER FUELS',
                           'FURNISHINGS, HOUSEHOLD EQUIPMENT AND MAINTENANCE',
                           'FURNITURE & CARPETS',
                           'HOUSEHOLD TEXTILES',
                           'HOUSEHOLD APPLIANCES',
                           'HOUSEHOLD UTENSILS',
                           'TOOLS FOR HOUSE & GARDEN',
                           'GOODS FOR HOUSEHOLD MAINTENANCE',
                           'HEALTH',
                           'MEDICAL PRODUCTS & EQUIPMENT',
                           'OUTPATIENT SERVICES',
                           'HOSPITAL SERVICES',
                           'TRANSPORT',
                           'PURCHASE OF VEHICLES',
                           'OPERATION OF TRANSPORT EQUIPMENT',
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
                           'INSURANCE',
                           'FINANCIAL SERVICES N.E C.',
                           'OTHER SERVICES N.E.C.'
                           ] 

        # Setup DataFrame with multi-level columns and no initial rows
        self.cityIndexDf = pd.DataFrame(columns=multicolumns)
        self.cityIndexDf.index.name = "Category"  # Naming the index for clarity

        # Set the path for the Tesseract engine executable
        pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        self.poppler_path = r'C:\\Users\\amjad\\Downloads\\poppler-24.02.0\\library\\bin'

    def ocr_images(self, images):
        # # Perform OCR on each image and collect texts from images containing "Table 4"
        # all_text = []
        # for img in images:
        #     text = pytesseract.image_to_string(img, lang='eng')
        #     if 'Table 4' in text:
        #         all_text.append(text)
        # return all_text
        # Perform OCR on each image and collect texts from images containing "Table 4",
        # but skip every other image containing "Table 4" starting from the first one found.
        all_text = []
        # found_table_4 = False  # Flag to indicate if "Table 4" has been found
        # count_table_4 = 0  # Counter for images with "Table 4"

        for img in images:
            text = pytesseract.image_to_string(img, lang='eng')
            # if 'Table 4' in text and 'JAN DEC' not in text:
            if 'Table 4' in text and not any(element in text for element in ['JAN DEC', 'MAR FEB', 'MAY APR', 'JUL JUN', 'SEP AUG', 'NOV OCT']):
                # count_table_4 += 1  # Increment counter each time "Table 4" is found
                # Calculate the current set (group of 8) this image belongs to
                # current_set = (count_table_4 - 1) // 8
                # if found_table_4 and skip_next:
                #     # If "Table 4" was found before and we're skipping this one, reset skip_next
                #     skip_next = False
                #     continue  # Skip this image
                # if found_table_4 and not skip_next:
                #     # If "Table 4" was found before and this one is not being skipped,
                #     # add its text and set skip_next for the next occurrence
                #     all_text.append(text)
                #     skip_next = True
                # if not found_table_4:
                #     # If this is the first time "Table 4" is found, skip it and mark subsequent finds for addition
                #     found_table_4 = True
                #     skip_next = True
                # Determine if this image is in a set to be processed or skipped
                # if current_set % 2 == 0:
                # Even sets (0-based) are skipped, so do nothing here
                # continue
                # else:
                # Odd sets are processed
                # all_text.append(text)
                all_text.append(text)
            # If "Table 4" is not found in the text, no action is required
        return all_text

    def evaluate(self, images):
        all_text = []

        for img in images:
            text = pytesseract.image_to_string(img, lang='eng')
            # have to check JAN and DEC
            if 'Table 4' in text and any(element in text for element in ['MAR FEB', 'MAY APR', 'JUL JUN', 'SEP AUG', 'NOV OCT']):
                all_text.append(text)
        return all_text

    def convert_pdf_to_image(self, pdf_path):
        # Convert PDF to images, one image per page
        return pdf2image.convert_from_path(pdf_path, poppler_path=self.poppler_path)

    def process_pdf(self, pdf_path):
        # Convert PDF to images, then extract text using OCR for pages containing "Table 4"
        images = self.convert_pdf_to_image(pdf_path)
        extracted_texts = self.ocr_images(images)
        return extracted_texts

    def year_months_cities(self, text):
        """input: all the data in one page
        loop and find cities, months and year
        output: two list of two index and a number"""
        found_year = None
        found_months = []
        found_cities = []
        city_name_variants = {
            "jazzan": "JAZAN",
            "alhofuf": "ALHOFOF",
            "hofhuf": "ALHOFOF",
        }
        year_re = re.compile(r'(2012|2013|2014)')
        year_match = year_re.search(text)
        if year_match:
            found_year = int(year_match.group())

        month_pattern = r'\b(' + '|'.join(self.months) + r')\b'
        all_month_matches = re.finditer(month_pattern, text, re.IGNORECASE)
        for match in all_month_matches:
            found_month = match.group().upper()
            if found_month not in found_months:
                found_months.append(found_month)
            if len(found_months) == 2:
                break
            
        # Normalize city names in the combined_text
        normalized_text = text.lower()
        for variant, standard in city_name_variants.items():
            normalized_text = normalized_text.replace(
                variant, standard.lower())

        for city in self.cities:
            if city.lower() in normalized_text.lower():
                found_cities.append(city)
                if len(found_cities) == 2:
                    break

        if found_year and len(found_months) == 2 and len(found_cities) == 2:
            return (found_year, found_months, found_cities)
        else:
            return None

    def values(self, text, rowIndices):
        """input: data and self.rowIndices
        to do: loop through data then when you find rowIndices then get the line.
        1st, 2ed, 4ed, 5ed numbers
        output: ([rowIndix], [list of 4 numbers])"""
        # data = {}
        # for rowIndex in rowIndices:
        #     pattern = re.compile(rowIndex + r'.*?(\d+\.\d+)')  # Adjust pattern as needed
        #     matches = pattern.findall(text)
        #     if matches:
        #         data[rowIndex] = [float(num) for num in matches[:4]]  # Assuming 4 numbers of interest
        # return data
        data = {}
        for rowIndex in rowIndices:
            for line in text.split('\n'):
                match = re.search(r'^\D*', line)
                matched_string = match.group(0) if match else ''
                if rowIndex == matched_string.strip():
                    # Use regex to extract all numbers from the line
                    numbers = re.findall(r'-?\d+\.\d+', line)
                    if numbers:
                        data[rowIndex] = [float(num) for num in numbers]
        return data

    def mach(self,  values_to_assign, rowIndex, found_year, found_months, found_cities):
        """mach:
                one = [found_cities[0], found_year,
               found_months[0], rowIndex, values_to_assign[3]]
        two = [found_cities[0], found_year,
               found_months[1], rowIndex, values_to_assign[2]]
        three = [found_cities[1], found_year,
                 found_months[0], rowIndex, values_to_assign[1]]
        four = [found_cities[1], found_year,
                found_months[1], rowIndex, values_to_assign[0]]
            output: return (one, two, three, four)"""
        data = []
        numbers = values_to_assign.copy()
        if len(numbers) < 6:
            print(
                f"Row not read properly. Cities: {found_cities}, RowIndex: {rowIndex}, Year: {found_year}, Months: {found_months}")
            return data

        if len(found_cities) == 2 and len(found_months) == 2:
            # values are in a specific order
            data.append([found_cities[0], found_year,
                        found_months[1], rowIndex, numbers[4]])
            data.append([found_cities[0], found_year,
                        found_months[0], rowIndex, numbers[3]])
            data.append([found_cities[1], found_year,
                        found_months[1], rowIndex, numbers[1]])
            data.append([found_cities[1], found_year,
                        found_months[0], rowIndex, numbers[0]])
        return data

    def check(self, city, year, month, rowIndex, expected_value):
        """
        Check if the value in the DataFrame for the specified city, year, month, and rowIndex
        matches the expected value. If not, print the discrepancy.
        """
        # actual_value = self.cityIndexDf.loc[rowIndex, (city, year, month)]
        # if actual_value != expected_value:
        #     print(
        #         f"Discrepancy found: City: {city}, Month: {month}, Expected: {expected_value}, Actual: {actual_value}")
        try:
            actual_value = self.cityIndexDf.loc[rowIndex, (city, year, month)]
            if actual_value != expected_value:
                print(
                    f"Discrepancy found: City: {city}, Month: {month}, {rowIndex}, Expected: {expected_value}, Actual: {actual_value}")
            # If actual value is NaN, update it with expected_value
            if pd.isnull(actual_value):
                self.cityIndexDf.loc[rowIndex,
                                     (city, year, month)] = expected_value
                print(
                    f"Filled missing value for {city}, {year}, {month}, {rowIndex} with expected value: {expected_value}")

        except KeyError:
            print(
                f"Data not found for City: {city}, Year: {year}, Month: {month}, Category: {rowIndex}")

    def process(self, pdf_path):
        """Main method to process the PDF file.
        """
        images = self.convert_pdf_to_image(pdf_path)
        extracted_texts = self.ocr_images(images)

        for text in extracted_texts:
            found_year, found_months, found_cities = self.year_months_cities(
                text)
            values_to_assign = self.values(text, self.rowIndices)
            # Iterate through each rowIndex and its associated values
            for rowIndex, values in values_to_assign.items():
                matched_data = self.mach(
                    values, rowIndex, found_year, found_months, found_cities)

                for data in matched_data:
                    city, year, month, rowIndex, value = data
                    # 'city', 'year', and 'month' are columns in DataFrame
                    self.cityIndexDf.loc[rowIndex, (city, year, month)] = value

    def evaluate_process(self, pdf_path):
        """
        Process the PDF file like the 'process' method but includes validation checks
        to ensure the DataFrame has correct values after processing.
        """
        images = self.convert_pdf_to_image(pdf_path)
        extracted_texts = self.evaluate(images)  # Using evaluate to get text

        for text in extracted_texts:
            # Store the result of year_months_cities
            result = self.year_months_cities(text)
            if result is None:
                # Handle the case where year_months_cities returns None.
                continue  # Skip to the next iteration of the loop

            found_year, found_months, found_cities = self.year_months_cities(
                text)
            values_to_assign = self.values(text, self.rowIndices)

            for rowIndex, values in values_to_assign.items():
                matched_data = self.mach(
                    values, rowIndex, found_year, found_months, found_cities)

                for data in matched_data:
                    city, year, month, rowIndex, expected_value = data
                    self.check(city, year, month, rowIndex,
                               expected_value)  # Validation check


# %%
ocr_alt = OCRAAlt()
#%%
pdf_path = '../data/2014.pdf'
ocr_alt.process(pdf_path)
ocr_alt.evaluate_process(pdf_path)
# %%
pdf_path2 = '../data/2012.pdf'
ocr_alt.process(pdf_path2)
ocr_alt.evaluate_process(pdf_path2)
#%%
pdf_path3 = '../data/2013.pdf'
ocr_alt.process(pdf_path3)
ocr_alt.evaluate_process(pdf_path3)

#%%
# Count unique cities, years, and categories
num_cities = ocr_alt.cityIndexDf.columns.get_level_values('City').nunique()
num_years = ocr_alt.cityIndexDf.columns.get_level_values('Year').nunique()
num_categories = ocr_alt.cityIndexDf.index.nunique()

print(f"Number of unique cities: {num_cities}")
print(f"Number of unique years: {num_years}")
print(f"Number of unique categories: {num_categories}")
# %%

# Total number of values in the DataFrame
total_values = ocr_alt.cityIndexDf.size

# Count NaN values in the DataFrame
nan_count = ocr_alt.cityIndexDf.isna().sum().sum()

# Calculate the proportion of NaN values
nan_proportion = nan_count / total_values

print(f"Total number of values: {total_values}")
print(f"Total number of NaN values: {nan_count}")
print(f"Proportion of NaN values: {nan_proportion:.2%}")  # formatted as a percentage

# %%
#import openpyxl
# Save DataFrame to Excel file
ocr_alt.cityIndexDf.to_excel('cityIndexData.xlsx', sheet_name='City Data', engine='openpyxl')

# %%
