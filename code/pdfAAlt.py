# %%
# pip install pdfplumber
import pdfplumber
import os
import pandas as pd
import re

# %%


class pdfAA:
    """
    Read special pdf files to extract info and create dataframe
    """

    def __init__(self, pdf_path=""):
        """
        contructor
        """
        # self.cities = ["MAKKAH", "RIYADH", "TAIF", "JEDDAH", "BURAYDAH", "MEDINA", "HOFHUF", "DAMMAM", "TABUK", "ABHA", "Jazan", "Hail",
        #                "Baha", "Njran", "Arar", "Skaka"]  # up to page 18 on 2003.pdf. Bottom of page says page 19. Why some all caps in the pdf??
        self.cities = [
            "MAKKAH", "RIYADH", "TAIF", "JEDDAH", "BURAYDAH", "MEDINA",
            "ALHOFOF", "DAMMAM", "TABUK", "ABHA", "JAZAN", "HAIL", "BAHA",
            "NJRAN", "ARAR", "SKAKA"
        ]

        self.months = ["JAN", "FEB", "MAR", "APR", "MAY",
                       "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

        self.years = list(range(2002, 2011))  # from 2002 - 2015

        multicolumns = pd.MultiIndex.from_product(
            [self.cities, self.years, self.months], names=['City', 'Year', 'Month'])

        self.rowIndices = ["General Index", "Foodstuffs", "Cereals and cereal products", "Meat and Poultry", "Fish and crustaceans", "Milk and dairy products", "Eggs", "Cooking oil and fats", "Fresh vegetables", "Preserved and canned vegetables", "Legumes and tubers", "Fresh fruits", "Preserved and canned fruits", "Nuts, peanuts, seeds", "Sugars and sugar preparations", "Beverages", "Foodstuffs, other", "Tobacco", "Out-of-home meals", "Fabrics, clothing and footwear", "Men's fabrics", "Women's fabrics", "Men's apparel", "Women's apparel", "Tailoring", "Footwear", "House and related items", "Home repairs", "Rents", "Water supply expenditure", "Fuel and Power", "Home furniture",
                           "Furniture and carpet", "Home furnishings", "Small home appliances", "kitchenhouse & tabletualis", "Household small items", "Home services", "Basic home appliances", "Medical care", "Medical care expenses", "Other medical expenses", "Medicines", "Transport and telecommunications", "Private transport means", "Operation of private transport means", "Public transport fees", "Telecommunications and related costs", "Education and entertainment", "Entertainment expenses", "Education expenses", "Entertainment devices", "Other expenses and services", "Personal hygiene and care items", "Personal goods", "Other expenses and services"]  # taken from page 12 of 2003.pdf. Bottom of page says page 19.

        # three-level column heads. Store all info here.
        self.cityIndexDf = pd.DataFrame(
            index=self.rowIndices, columns=multicolumns)
        self.currPdfPath = pdf_path
        # save each page's text into a df
        self.currFileTextDf = pd.DataFrame(columns=['text'])
        # indexed by page number, column has the text value.
        self.currFileTextDf.index.name = "page"
        return

    def importPdf(self, pdf_path="", xoffsetleft=0, xoffsetright=0, yoffsettop=0, yoffsetbottom=0, width=0, height=0):
        """
        Import and read pdf
        Args:
            pdf_path (str, optional): _description_. Defaults to "".
            xoffset (int, optional): _description_. Defaults to 0.
            yoffset (int, optional): _description_. Defaults to 0.
        """
        if not pdf_path:
            pdf_path = self.currPdfPath
        if len(self.currFileTextDf):
            # delete everything and starts new if already existed
            self.currFileTextDf = self.currFileTextDf.iloc[0, 0]
        with pdfplumber.open(pdf_path) as pdf:
            for i, page in enumerate(pdf.pages):
                # Define the bounding box (crop box) for the first column
                # The bounding_box is in the format (x0, top, x1, bottom), with:
                # x0: the left edge of the column
                # top: the top edge of the column (usually 0 to start from the top)
                # x1: the right edge of the column
                # bottom: the bottom edge of the column (use page.height to cover until the bottom of the page)
                pagewidth = width if width > 0 else page.width/2 - xoffsetleft
                pageheight = height if height > 0 else page.height - yoffsettop - yoffsetbottom
                bounding_box = (xoffsetleft, yoffsettop, pagewidth, pageheight)

                # Crop the page to the bounding box to focus on the first column
                cropped_page = page.within_bbox(bounding_box)

                # Extract text from the cropped area
                text = cropped_page.extract_text()

                self.currFileTextDf.loc[i, 'text'] = text

                # if text:
                #     print(f"Page {i+1} First Column:\n{text}\n")
                # else:
                #     print(f"Page {i+1} First Column: No text found\n")

    def checkPageType(self, pageText):
        """
        Check if the page is about cities
        Args:
            pageText (str): the entire page of text from pdf
        """
        pattern = re.compile(r'Table 4', re.IGNORECASE)
        # return True / False, or return "city", "quarterAnnual", and different types if applicable, etc
        if pattern.search(pageText):
            return True
        else:
            return False

    def pullCityYearMonthValues(self, pageText, city=0):
        """
        if pageType is correct, pull Year-Month values from first column somehow, along with the one-or-two city name(s)
        Args:
            pageText (str): the entire page of text from pdf
            city (int): 0 or 1, for the two different city values on a typial page. Not sure if some page might only have 1 city.
            return: [ city, year, month ] list
        """
        # let's find the first mention of any year
        # found_year = "Unknown"
        # for year in self.years:
        #     if str(year) in pageText:
        #         found_year = year
        #         break  # Exit once the first year is found
        city_name_variants = {
            "jazzan": "JAZAN",
            "alhofuf": "ALHOFOF",
            "hofhuf": "ALHOFOF",
        }
        match = re.search(r'\b(200[2-9]|201[01])\b', pageText)
        if match:
            # Extract the first year found in the text
            found_year = match.group(0)
        else:
            # If no year is found, return "Unknown"
            found_year = "Unknown"

            return found_year
        # Normalize the page text to simplify matching
        normalized_text = pageText.upper()
        for variant, correct in city_name_variants.items():
            normalized_text = normalized_text.replace(variant.upper(), correct)

        # Search for city names directly in the text
        found_city = "Unknown"
        for city_name in self.cities:
            if city_name in normalized_text:  # Check using the normalized city names
                found_city = city_name
                break  # Exit the loop once the first city name is found

        # let's find the first mention of any month
        # found_month = "Unknown"
        # for month in self.months:
        #     if month in pageText:
        #         found_month = month
        #         break  # Exit once the first month is found
        month_pattern = r'\b(' + '|'.join(self.months) + r')\b'
        # Search for the pattern in the text, making the search case-insensitive
        match = re.search(month_pattern, pageText, re.IGNORECASE)
        if match:
            # Extract the first month abbreviation found in the text
            # Ensure the found month is in uppercase to match your list
            found_month = match.group(0).upper()
        else:
            # If no month is found, return "Unknown"
            found_month = "Unknown"
            # return found_month

        if found_city != "Unknown" and found_year != "Unknown" and found_month != "Unknown":
            return [found_city, int(found_year), found_month]
        else:
            # Handle the case where necessary information is not found
            return ["Unknown", 0, "Unknown"]

    def pullRowNameAndValues(self, rowText, city=0):
        """
        For each row in pageText, see if it corresponds to an expenditure group item. If so, pull the group name, and the first column value
        Args:
            rowText (str): a row of text in pageText
            city (int): 0 or 1, for the two different city values on a typial page. Not sure if some page might only have 1 city.
            return: [ expenditureGroup, value ] list
        """
        # result = None
        # result = [ "General Index", 101.60 ] # for example
        # return result
        # If the two above steps are successful, can save the values into
        # self.cityIndexDf.loc[ resultFromPullRow[0], [resultFromPullCity] ] = resultFromPullRow[1]
        # Try to match the row text with any of the predefined row indices (expenditure group names)
        for rowIndex in self.rowIndices:
            match = re.search(r'^\D*', rowText)
            matched_string = match.group(0)
            # match = re.search(rowIndex, re.search(r'^\D*', rowText) , re.IGNORECASE)
            if rowIndex == matched_string.strip():
                # Extract the first year found in the text
                # found_year = match.group(0)
                # if rowText.startswith(rowIndex):
                # After finding a matching expenditure group, extract the next float value in the text
                # This regex looks for a sequence of digits possibly followed by a decimal point and more digits
                value_pattern = re.compile(r'(\d+\.\d+|\d+)')
                value_match = value_pattern.search(
                    rowText[len(rowIndex):].strip())

                if value_match:
                    # Convert the matched numeric string to a float
                    value = float(value_match.group(0))
                    return [rowIndex, value]

        # If no matching expenditure group or value is found, return None
        return None

    def processPages(self):
        for index, row in self.currFileTextDf.iterrows():
            pageText = row['text']
            if self.checkPageType(pageText):
                cityYearMonth = self.pullCityYearMonthValues(pageText)
                # this means a successful extraction
                if cityYearMonth != ["Unknown", 0, "Unknown"]:
                    # split the pageText into individual rows
                    # pageText.split('\n')
                    for rowText in pageText.split('\n'):
                        rowValues = self.pullRowNameAndValues(rowText)
                        if rowValues:  # If rowValues is not None
                            # update the DataFrame with the extracted values
                            # rowValues = [expenditureGroup, value]
                            # cityYearMonth = [city, year, month]
                            self.cityIndexDf.loc[rowValues[0], (
                                cityYearMonth[0], cityYearMonth[1], cityYearMonth[2])] = rowValues[1]


# %%
# Instantiate
# pdf_path = "/Users/amjad/OneDrive/المستندات/GWU_Cources/Spring2024/capstone_project/data/2003.pdf"
# pdf_path = "../data/2003_sample.pdf"
pdf_path = "../data/2003.pdf"
thepdf = pdfAA()
thepdf.importPdf(pdf_path,xoffsetleft=0.4)
# for some reason it takes the value of the next month and add it to the index of this month
thepdf.processPages()
# thepdf.importPdf(pdf_path)

# %%
pdf_path2 = "../data/2002.pdf"
thepdf = pdfAA()
thepdf.importPdf(xoffsetleft=0.4)
# for some reason it takes the value of the next month and add it to the index of this month
thepdf.processPages()
