
# %%
import os
import glob
import pandas as pd
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
            "HOFHUF", "DAMMAM", "TABUK", "ABHA", "Jazan", "Hail", "Baha",
            "Njran", "Arar", "Skaka"
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

        # Initialize rowIndices as an empty list
        self.rowIndices = []

        # Setup DataFrame with multi-level columns and no initial rows
        self.cityIndexDf = pd.DataFrame(columns=multicolumns)
        self.cityIndexDf.index.name = "Category"  # Naming the index for clarity

        # Variables for Excel file processing
        self.currExcelPath = excel_path  # Current Excel file path
        self.data = pd.DataFrame()

    def process_sheet_by_name(self, file_path, sheet_name):
        """
        Processes a single sheet by its name from the given Excel file.
        """
        # Ensure the file_path is correctly used to refer to the Excel file
        print(f"Processing sheet '{sheet_name}' from file '{file_path}'")
        try:
            df = pd.read_excel(file_path, sheet_name=sheet_name)
            df.dropna(axis=0, how='all', inplace=True)
            df.dropna(axis=1, how='all', inplace=True)
            # Further processing steps can be added here
        except Exception as e:
            print(
                f"Error processing sheet '{sheet_name}' in file '{file_path}': {e}")

    def process_files_in_directory(self, directory_path, file_pattern="*.xls*"):
        """
        Iterates over Excel files in a directory, processing sheets with '4' in their name.
        """
        for file_path in glob.glob(os.path.join(directory_path, file_pattern)):
            print(f"Processing file: {file_path}")
            try:
                sheet_names = pd.ExcelFile(file_path).sheet_names
                for sheet_name in sheet_names:
                    if '4' in sheet_name:
                        self.process_sheet_by_name(file_path, sheet_name)
            except Exception as e:
                print(f"Error processing file '{file_path}': {e}")


# %%
file_path = '../data/2016/'
extractor = excelAAlt()
extractor.process_files_in_directory(file_path)


# %%
