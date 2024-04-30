
# # %%
# import pandas as pd
# import os
# import glob
# import datetime
# import re
# # %%
# def extract_month_year(text):
#     # pattern to account for extra spaces and format variations
#     # \s* allows for any number of spaces
#     match = re.search(r'(\w+)\s+\d{4}', text)
#     if match:
#         # Extract the entire matched string to further process for month and year
#         matched_string = match.group(0)
#         # Splitting the matched string by spaces and taking the last two elements
#         # should give us the month name and year, even with extra spaces in between
#         parts = matched_string.split()
#         month = parts[-2]  # Second last element should be the month name
#         year = parts[-1]  # Last element should be the year
#         # Ensure we only capture valid month names by trying to parse it
#         try:
#             datetime.datetime.strptime(month, '%B')
#             return month, year
#         except ValueError:
#             # The month name wasn't valid (e.g., not a real month name), return None
#             return None, None
        
#     return None, None

# # Function to read the fourth sheet and extract month and year from the first row
# def read_fourth_sheet_with_date(file_path):
#     # Read just the first row to examine the headers
#     first_row = pd.read_excel(file_path, sheet_name=3, nrows=1)
    
#     # Initialize month and year
#     month, year = None, None

#     # Iterate over column names to find a column with the date information in its name
#     for col_name in first_row.columns:
#         # The column name itself might contain the month and year
#         month, year = extract_month_year(col_name)  # Attempt to extract month and year directly from the column name
#         if month and year:  # If both month and year are successfully extracted
#             break  # Exit the loop as we've found the date information

#     # Now read the rest of the sheet, skipping the first row
#     df = pd.read_excel(file_path, sheet_name=3, skiprows=1)

#     # Add the 'month' and 'year' columns
#     df['month'] = month
#     df['year'] = year

#     return df


# # %%
# # Get a list of all xlsx files
# file_list = glob.glob('../data/2023/*.xlsx')

# # Read all files and concatenate into a single dataframe
# price = pd.concat([read_fourth_sheet_with_date(file)
#                    for file in file_list], ignore_index=True)

# price

# # %%
# import pandas as pd
# import datetime
# import glob
# import re
# #%%
# class DataExtractor:
#     def __init__(self):

#         self.years = list(range(2020, 2023))  # Example range
#         self.cities = [
#             "MAKKAH", "RIYADH", "TAIF", "JEDDAH", "BURAYDAH", "MEDINA",
#             "ALHOFOF", "DAMMAM", "TABUK", "ABHA", "JAZAN", "HAIL", "BAHA",
#             "NJRAN", "ARAR", "SKAKA"
#         ]
#         self.months = [
#             "JAN", "FEB", "MAR", "APR", "MAY", "JUN",
#             "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"
#         ]
#         multicolumns = pd.MultiIndex.from_product(
#             [self.cities, self.years, self.months],
#             names=['City', 'Year', 'Month']
#         )
#         self.cityIndexDf = pd.DataFrame(columns=multicolumns)
#         self.cityIndexDf.index.name = "Category"

#     def extract_month_year(self, header):
#         """ Extract the month and year from the table header or file name. """
#         match = re.search(r'(\w+) (\d{4})', header)
#         if match:
#             month, year = match.groups()
#             return month, int(year)
#         return None, None

#     def process_data_sheet(self, df, month, year):
#         """ Process a DataFrame of CPI data to fit into cityIndexDf """
#         if month and year:
#             month_index = self.months.index(month) + 1  # Convert month name to number
#             for index, row in df.iterrows():
#                 category = row['Expenditure Category:'].strip()
#                 for city in self.cities:
#                     value = row.get(city)
#                     if pd.notna(value):  # Check if there is a valid number
#                         self.cityIndexDf.at[(category, city, year, month_index), :] = value

#     def read_sheet_with_data(self, file_path):
#         """ Read data from a specific Excel sheet and extract CPI data """
#         df = pd.read_excel(file_path, sheet_name=3)  # Assuming data is in the first sheet
#         header = df.columns[0]
#         month, year = self.extract_month_year(header)
#         self.process_data_sheet(df.iloc[1:], month, year)  # Skip the first row if it's headers

#     def process_files(self, directory, file_pattern="*.xlsx"):
#         """ Process all Excel files in the specified directory """
#         file_path_pattern = f"{directory}/{file_pattern}"
#         file_list = glob.glob(file_path_pattern)
#         # for each file find 
#         # then get extract month and the year
#         #then 
# #%%
# # Example usage
# data_extractor = DataExtractor()
# df_final = data_extractor.process_files('../data/2022')
# print(df_final)

# #%%
# # Usage
# data_extractor = DataExtractor()
# df_final = data_extractor.process_files('../data/2023')
# print(df_final)


# %%
import pandas as pd
import datetime
import re
import glob

class DataExtractor:
    def __init__(self):
        self.cities = [
            "MAKKAH", "RIYADH", "TAIF", "JEDDAH", "BURAYDAH", "MEDINA",
            "ALHOFOF", "DAMMAM", "TABUK", "ABHA", "JAZAN", "HAIL", "BAHA",
            "NJRAN", "ARAR", "SKAKA"
        ]
        self.months = [
            "JAN", "FEB", "MAR", "APR", "MAY", "JUN",
            "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"
        ]
        self.years = list(range(2020, 2024))

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
        self.cityIndexDf = pd.DataFrame(index=self.rowIndices, columns=multicolumns)
        self.cityIndexDf.index.name = "Category"
        # self.category_norm = {"HOUSING, WATER, ELECTRI-CITY GAS AND OTHER FUELS" : "HOUSING, WATER, ELECTRICITY, GAS AND OTHER FUELS",
        # "RENTALS FOR HOUSING": "ACTUAL RENTALS FOR HOUSING",
        # "MAITENANCE OF THE DEWELLING": "MAINTENANCE AND REPAIR OF THE DWELLING",
        # "WATER SUPPLY & OTHER SERVICES": "WATER SUPPLY AND MISCELLANEOUS SERVICES RELATING TO THE DWELLING",
        # "FURNISHINGS, HOUSEHOLD EQUIPMENT AND MAINTENANCE": "FURNISHINGS, HOUSEHOLD EQUIPMENT AND ROUTINE HOUSEHOLD MAINTENANCE",
        # "FURNITURE & CARPETS": "FURNITURE AND FURNISHINGS, CARPETS AND OTHER FLOOR COVERINGS",
        # "OPERATION OF TRANSPORT EQUIPMENT": "OPERATION OF PERSONAL TRANSPORT EQUIPMENT",
        # "AUDIO, PHOTO & INFO. EQUIPMENT":"AUDIO-VISUAL, PHOTOGRAPHIC AND INFORMATION PROCESSING EQUIPMENT",
        # "OTHER RECREATION & CULTURE GOODS":"OTHER MAJOR DURABLES FOR RECREATION AND CULTURE",
        # "OTHER RECREATIONAL GOODS":"OTHER RECREATIONAL ITEMS AND EQUIPMENT, GARDENS, AND PETS",
        # "RECREATIONAL & CULTURAL SERVICES": "RECREATIONAL AND CULTURAL SERVICES",
        # "NEWSPAPERS, BOOKS & STATIONERY":"NEWSPAPERS, BOOKS AND STATIONARY",
        # "PRE-PRIMARY & PRIMARY EDUCATION": "PRE-PRIMARY AND PRIMARY EDICATION",
        # "SECONDARY&INTERMEDIATE EDUCATION": "SECONDARY EDUCATION",
        # "POST-SECONDARY EDUCATION": "POST-SECONDARY NON-TERTIARY EDUCATION",
        # "CATERING SERVICE":"CATERING SERVICES", "FINANCIAL SERVICES N.E C.": "FINANCIAL SERVICES N.E.C."
        #     }
        self.category_norm= {
        "HOUSING, WATER, ELECTRICITY, GAS AND OTHER FUELS": "HOUSING, WATER, ELECTRI-CITY GAS AND OTHER FUELS",
        "ACTUAL RENTALS FOR HOUSING": "RENTALS FOR HOUSING",
        "MAINTENANCE AND REPAIR OF THE DWELLING": "MAITENANCE OF THE DEWELLING",
        "WATER SUPPLY AND MISCELLANEOUS SERVICES RELATING TO THE DWELLING": "WATER SUPPLY & OTHER SERVICES",
        "FURNISHINGS, HOUSEHOLD EQUIPMENT AND ROUTINE HOUSEHOLD MAINTENANCE": "FURNISHINGS, HOUSEHOLD EQUIPMENT AND MAINTENANCE",
        "FURNITURE AND FURNISHINGS, CARPETS AND OTHER FLOOR COVERINGS": "FURNITURE & CARPETS",
        "OPERATION OF PERSONAL TRANSPORT EQUIPMENT": "OPERATION OF TRANSPORT EQUIPMENT",
        "AUDIO-VISUAL, PHOTOGRAPHIC AND INFORMATION PROCESSING EQUIPMENT": "AUDIO, PHOTO & INFO. EQUIPMENT",
        "OTHER MAJOR DURABLES FOR RECREATION AND CULTURE": "OTHER RECREATION & CULTURE GOODS",
        "OTHER RECREATIONAL ITEMS AND EQUIPMENT, GARDENS, AND PETS": "OTHER RECREATIONAL GOODS",
        "RECREATIONAL AND CULTURAL SERVICES": "RECREATIONAL & CULTURAL SERVICES",
        "NEWSPAPERS, BOOKS AND STATIONARY": "NEWSPAPERS, BOOKS & STATIONERY",
        "PRE-PRIMARY AND PRIMARY EDICATION": "PRE-PRIMARY & PRIMARY EDUCATION",
        "SECONDARY EDUCATION": "SECONDARY&INTERMEDIATE EDUCATION",
        "POST-SECONDARY NON-TERTIARY EDUCATION": "POST-SECONDARY EDUCATION",
        "CATERING SERVICES": "CATERING SERVICE",
        "FINANCIAL SERVICES N.E.C.": "FINANCIAL SERVICES N.E C."
    }

    def extract_month_year(self, text):
        match = re.search(r'(\w+)\s+\d{4}', text)
        if match:
            matched_string = match.group(0)
            parts = matched_string.split()
            month = parts[-2].upper()
            year = parts[-1]
            try:
                datetime.datetime.strptime(month, '%B')
                return month[:3], year  # Return abbreviated month to match self.months
            except ValueError:
                return None, None
        return None, None

    def read_fourth_sheet_with_date(self, file_path):
        first_row = pd.read_excel(file_path, sheet_name=3, nrows=1)
        month, year = None, None
        for col_name in first_row.columns:
            month, year = self.extract_month_year(col_name)
            if month and year:
                break
        df = pd.read_excel(file_path, sheet_name=3, skiprows=1)
        df['month'] = month
        df['year'] = year
        return df
    
    def normalize_city_names(self, df):
        # Dictionary of known city name variants
        city_name_variants = {
            "jazzan": "JAZAN",
            "alhofuf": "ALHOFOF",
            "hofhuf": "ALHOFOF",
        }

        normalized_columns = []
        for col in df.columns:
            if col.lower() not in ['month', 'year', 'expenditure category:']:  # Preserve certain column names
                normalized_col = col.lower()
                for variant, standard in city_name_variants.items():
                    if variant in normalized_col:
                        normalized_col = normalized_col.replace(variant, standard.lower())
                normalized_columns.append(normalized_col.upper())  # Use upper case for final column names
            else:
                normalized_columns.append(col)  # Keep 'month' and 'year' as is

        df.columns = normalized_columns
        return df
    
    def normalize_category(self, category):
        return self.category_norm.get(category, category)

    def integrate_data(self, combined_df):
        # Normalize city names in the DataFrame
        combined_df = self.normalize_city_names(combined_df)
        #combined_df['Expenditure Category:'] = combined_df['Expenditure Category:'].apply(self.normalize_category)

        # Iterate through each row in the DataFrame
        for idx, row in combined_df.iterrows():
            month = row['month']
            year = int(row['year']) 
            # category = row['Expenditure Category:']  
            category = self.normalize_category(row['Expenditure Category:'])

            # normalized_category = category_norm.get(original_category.strip(), original_category.strip())
            #df['Expenditure Category:'] = df['Expenditure Category:'].apply(lambda x: normalize_category(x, category_norm))

            # Update the cityIndexDf for each city
            for city in self.cities:
                if city in combined_df.columns:
                    value = row[city]  # Value for that city/category
                    if pd.notna(value):
                        self.cityIndexDf.loc[category, (city, year, month)] = value
                        
    def process_files(self, directory):
        file_pattern = f"{directory}/*.xlsx"
        file_list = glob.glob(file_pattern)
        all_data = [self.read_fourth_sheet_with_date(file) for file in file_list]
        combined_df = pd.concat(all_data, ignore_index=True)
        combined_df = self.normalize_city_names(combined_df)  # Normalize city names first
        self.integrate_data(combined_df)
#%%
data_extractor = DataExtractor()
data_extractor.process_files('../data/2023')
data_extractor.process_files('../data/2022')
data_extractor.process_files('../data/2020')
data_extractor.process_files('../data/2021')
#%%
total_values = data_extractor.cityIndexDf.size

# Count NaN values in the DataFrame
nan_count = data_extractor.cityIndexDf.isna().sum().sum()

# Calculate the proportion of NaN values
nan_proportion = nan_count / total_values

print(f"Total number of values: {total_values}")
print(f"Total number of NaN values: {nan_count}")
print(f"Proportion of NaN values: {nan_proportion:.2%}")  # formatted as a percentage
#%%


data_extractor.cityIndexDf.to_excel('cityIndexData20233.xlsx', sheet_name='City Data', engine='openpyxl')
# %%
