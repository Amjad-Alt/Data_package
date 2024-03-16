
# %%
import pandas as pd
import os
import glob
import datetime
import re
# %%
def extract_month_year(text):
    # pattern to account for extra spaces and format variations
    # \s* allows for any number of spaces
    match = re.search(r'(\w+)\s+\d{4}', text)
    if match:
        # Extract the entire matched string to further process for month and year
        matched_string = match.group(0)
        # Splitting the matched string by spaces and taking the last two elements
        # should give us the month name and year, even with extra spaces in between
        parts = matched_string.split()
        month = parts[-2]  # Second last element should be the month name
        year = parts[-1]  # Last element should be the year
        # Ensure we only capture valid month names by trying to parse it
        try:
            datetime.datetime.strptime(month, '%B')
            return month, year
        except ValueError:
            # The month name wasn't valid (e.g., not a real month name), return None
            return None, None
        
    return None, None

# Function to read the fourth sheet and extract month and year from the first row
def read_fourth_sheet_with_date(file_path):
    # Read just the first row to examine the headers
    first_row = pd.read_excel(file_path, sheet_name=3, nrows=1)
    
    # Initialize month and year
    month, year = None, None

    # Iterate over column names to find a column with the date information in its name
    for col_name in first_row.columns:
        # The column name itself might contain the month and year
        month, year = extract_month_year(col_name)  # Attempt to extract month and year directly from the column name
        if month and year:  # If both month and year are successfully extracted
            break  # Exit the loop as we've found the date information

    # Now read the rest of the sheet, skipping the first row
    df = pd.read_excel(file_path, sheet_name=3, skiprows=1)

    # Add the 'month' and 'year' columns
    df['month'] = month
    df['year'] = year

    return df


# %%
# Get a list of all xlsx files
file_list = glob.glob('../data/2023/*.xlsx')

# Read all files and concatenate into a single dataframe
price = pd.concat([read_fourth_sheet_with_date(file)
                   for file in file_list], ignore_index=True)

price

# %%
