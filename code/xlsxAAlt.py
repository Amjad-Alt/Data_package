
# %%
import pandas as pd
import os
import glob
import datetime
import re
# %%
# Function to extract month and year from a string


def extract_month_year(text):
    # Match patterns like "May 2020"
    match = re.search(r'(\w+)\s(\d{4})', text)
    if match:
        month, year = match.groups()
        return month, year
    else:
        return None, None

# Function to read the fourth sheet and extract month and year from the first row


def read_fourth_sheet_with_date(file_path):
    # Read just the first row to examine the headers
    first_row = pd.read_excel(file_path, sheet_name=3, nrows=1)
    
    # Initialize month and year
    month, year = None, None

    # Check each of the first three columns for the date string
    for col in first_row.columns[:3]:
        header_text = first_row[col].values[0]
        if header_text and isinstance(header_text, str):
            month, year = extract_month_year(header_text)
            if month and year:
                break  # Stop searching once we've found a valid date
    # Now read the rest of the sheet, skipping the first row
    df = pd.read_excel(file_path, sheet_name=3, skiprows=1)

    # Add the 'month' and 'year' columns
    df['month'] = month
    df['year'] = year

    return df


# %%
# Get a list of all xlsx files
file_list = glob.glob('../data/2020/*.xlsx')

# Read all files and concatenate into a single dataframe
sprice = pd.concat([read_fourth_sheet_with_date(file)
                   for file in file_list], ignore_index=True)

sprice

# %%
