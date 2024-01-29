#%%
import json
import os
import shutil

#%%

def save_to_json(data, output_file_path):
    with open(output_file_path, 'w') as output_file:
        json.dump(data, output_file, indent=2)

semester2code = { "sp":"01", "spr":"01", "spring":"01", "su":"02", "sum":"02", "summer":"02", "fa":"03", "fall":"03"}
thisfilename = os.path.basename(__file__) # should match _ver for version, ideally 3-digit string starting as "000", up to "999"

data_to_save = \
    {
        # -----------------------------------------------------------------------------------------------------------------------
        "Version":
            """1""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Year":
            """2024""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Semester":
            """Spring""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_name":
            """Enhancing Data Usability: Comprehensive Cleaning and Packaging of Saudi Statistical Authority's Datasets""",
        "Objective":
            """ 
            The goal of this project is to create a comprehensive and cleaned dataset from the Saudi Arabian Statistical Authority, enhancing accessibility and usability for academic, governmental, and commercial purposes. This will facilitate more informed decision-making, research, and analysis across various sectors.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Dataset":
            """
            The dataset is going to be from the Saudi Arabian Statistical Authority, encompassing diverse statistical data ranging from demographics, economics, education, and healthcare. This comprehensive dataset will be invaluable for multifaceted analysis and research.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Rationale":
            """
            This project is going to help bridge the gap between raw data availability and practical usability. By cleaning and organizing the data, we make it more accessible and useful for researchers, policy-makers, and businesses, thereby fostering data-driven decision-making and innovation.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Approach":
            """
            I plan on approaching this capstone through several steps:

            1. Data Collection: Accessing and downloading relevant datasets from the Saudi Arabian Statistical Authority.
            2. Data Cleaning: Identifying and correcting inaccuracies, removing duplicates, and standardizing data formats.
            3. Data Analysis: Conducting preliminary analysis to understand data trends and characteristics.
            4. Data Packaging: Organizing the cleaned data into a user-friendly format, with comprehensive documentation.
            5. Validation: Ensuring data integrity and accuracy post-cleaning.
            6. Final Review: A thorough review of the dataset and accompanying documentation.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Timeline":
            """
            This is a rough timeline for this project:  

            - (1 Week) Data Collection
            - (2 Weeks) Data Cleaning 
            - (1 Week) Preliminary Data Analysis 
            - (4 Weeks) Data Packaging and Documentation
            - (2 Weeks) Validation of Data Integrity 
            - (2 Weeks) Final Review and Adjustments
            - (2 Weeks) Documentation Finalization and Submission
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Expected Number Students":
            """
            One student
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Possible Issues":
            """
            The challenges include ensuring data accuracy and integrity, dealing with potentially large and complex datasets, and addressing any missing or inconsistent data. Additionally, adhering to data privacy and security standards will be crucial throughout the project.
            """ ,
        # -----------------------------------------------------------------------------------------------------------------------
        "Proposed by": "Amjad Altuwayjiri",
        "Proposed by email": "amjadalt@gwu.edu",
        "instructor": "None",
        "instructor_email": "None",
        "github_repo": "https://github.com/Amjad-Alt/capstone_project",
        # -----------------------------------------------------------------------------------------------------------------------
    }
os.makedirs(
    os.getcwd() + f'{os.sep}Proposals{os.sep}{data_to_save["Year"]}{semester2code[data_to_save["Semester"].lower()]}{os.sep}{data_to_save["Version"]}',
    exist_ok=True)
output_file_path = os.getcwd() + f'{os.sep}Proposals{os.sep}{data_to_save["Year"]}{semester2code[data_to_save["Semester"].lower()]}{os.sep}{data_to_save["Version"]}{os.sep}'
save_to_json(data_to_save, output_file_path + "input.json")
shutil.copy(thisfilename, output_file_path)
print(f"Data saved to {output_file_path}")
