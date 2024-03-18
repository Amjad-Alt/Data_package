
# %%
import os
import glob
import pandas as pd
import re
# %%


class excelAAlt:
    """
    A class to extract data from Excel files (.xls and .xlsx), focusing on
    structured data extraction and organization into a pandas DataFrame.
    """

    def __init__(self, excel_path=""):
        """
        Constructor initializes the class with lists of cities, months, years,
        and sets up a multi-index DataFrame for storing extracted data.
        """
        self.cities = [
            "MAKKAH", "RIYADH", "TAIF", "JEDDAH", "BURAYDAH", "MEDINA",
            "HOFHUF", "DAMMAM", "TABUK", "ABHA", "JAZAN", "HAIL", "BAHA",
            "NJRAN", "ARAR", "SKAKA"
        ]
        self.months = [
            "JAN", "FEB", "MAR", "APR", "MAY", "JUN",
            "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"
        ]
        self.years = list(range(2015, 2017))

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

    def find_year_months_cities(self, df):
        found_year = None
        found_months = []
        found_cities = []

        combined_text = " ".join(df.iloc[:10].astype(str).values.flatten())
        year_re = re.compile(r'(2015|2016|2017)')
        year_match = year_re.search(combined_text)
        if year_match:
            found_year = int(year_match.group())

        for month in self.months:
            if month.lower() in combined_text.lower():
                found_months.append(month)
                if len(found_months) == 2:
                    break

        for city in self.cities:
            if city.lower() in combined_text.lower():
                found_cities.append(city)
                if len(found_cities) == 2:
                    break

        if found_year and len(found_months) == 2 and len(found_cities) == 2:
            return (found_year, found_months, found_cities)
        else:
            return None

    def extract_info_and_update(self, df, sheet_name):
        # Extract year, months, and cities
        info = self.find_year_months_cities(df)
        if info:
            year, months, cities = info
            # Instead of just printing, also call extract_and_assign_values
            self.extract_and_assign_values(
                df, year, months, cities, self.rowIndices)
        else:
            print(f"Could not extract info for '{sheet_name}'.")

    def process_sheet_by_name(self, file_path, sheet_name):
        try:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            self.extract_info_and_update(df, sheet_name)
        except Exception as e:
            print(
                f"Error processing sheet '{sheet_name}' in file '{file_path}': {e}")

    def process_files_in_directory(self, directory_path, file_pattern="*.xls*"):
        for file_path in glob.glob(os.path.join(directory_path, file_pattern)):
            try:
                sheet_names = pd.ExcelFile(file_path).sheet_names
                for sheet_name in sheet_names:
                    if '4' in sheet_name:
                        self.process_sheet_by_name(file_path, sheet_name)
            except Exception as e:
                print(f"Error processing file '{file_path}': {e}")

    def extract_and_assign_values(self, df, year, months, cities, rowIndices):
        start_row, start_col = self.find_starting_point(df, rowIndices)
        if start_row is None or start_col is None:
            return

        # Iterate through rowIndices and assign values to cityIndexDf
        for offset, rowIndex in enumerate(rowIndices):
            for city_index, city in enumerate(cities):
                for month_index, month in enumerate(months):
                    # Calculate the cell position; skipping every third value as required
                    if month_index == 2:  # Assuming the month index to skip is 2
                        continue
                    # Adjusted cell_pos to account for correct cell
                    cell_pos = city_index * 2 + month_index + 1
                    # Adjusted to use iloc for direct cell access
                    cell_value = df.iloc[start_row, start_col + cell_pos]

                    # Assign the extracted value to the DataFrame if it's a float
                    if isinstance(cell_value, float):
                        self.cityIndexDf.loc[(
                            city, year, month), rowIndex] = cell_value
                        print(
                            f"Assigned {cell_value} to {city}, {year}, {month}, {rowIndex}")

    def find_starting_point(self, df, rowIndices):
        for row in range(len(df)):
            for col in range(len(df.columns)):
                cell_value = str(df.iat[row, col])
                if any(rowIndex in cell_value for rowIndex in rowIndices):
                    return row, col
        return None, None


# %%
file_path = '../data/2015'
extractor = excelAAlt()
extractor.process_files_in_directory(file_path)
# %%
