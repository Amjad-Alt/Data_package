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
            """002""",
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
            The project's goal is to improve the way we handle data from the Saudi Arabian
            Statistical Authority, making it easier for everyone to use. We're setting up 
            a special pipeline to process and clean 22 different datasets. This process is fixable 
            and created to spot and fix various data issues, making sure the cleaned data is 
            both accurate and consistent. Our approach will 
            ensure the data we clean can be trusted and useful for many different uses, making it
            a valuable tool for anyone who needs it.""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Dataset":
            """
            The datasets are going to be from the Saudi Arabian Statistical Authority listing 
            the monthly average prices of various goods and services in the Kingdom of Saudi Arabia 
            for the year from 2002 to 2022, each year in a different file. The dataset includes a wide 
            range of categories such as food and beverages, meats and poultry, fish and seafood, dairy products and eggs
            , fruits and nuts, vegetables, oils and fats, along with other categories extending to construction materials, 
            personal care, and services.
            
            
            Several challenges that need to be addressed in this data. 
            These challenges include the presence of Arabic
            letters, empty columns, and non-organized lines. 
            Addressing these issues will make the dataset
            more accessible and usable for various analytical purposes.
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
            2. Data Cleaning: Creating a pipeline that identify and correct inaccuracies, remove duplicates, and standarize data formats.
            3. Pipeline Testing: After detecting patterns, test it on other datasets, then fix and modify as you go.
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
            - (1 Week) Pipeline Testing 
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

        Creating a data cleaning pipeline for a complex dataset involving Arabic text,
        empty columns, and non-organized lines presents several challenges. 
        These include handling encoding issues that can arise with Arabic characters, 
        ensuring accuracy in automated translations, dealing with missing or inconsistently
        formatted data, and developing custom cleaning rules for diverse data types.
        Additionally, maintaining the pipeline's efficiency and scalability, especially
        for large datasets, requires careful design to avoid long processing times.
        Ensuring data integrity throughout the cleaning process and adapting the
        pipeline to accommodate changes in data source formats or cleaning requirements
        are critical for preserving the quality and usability of the cleaned data.
        Rigorous testing and quality assurance are essential to address these challenges,
        necessitating a balance between automation and manual review to achieve accurate
        and reliable outcomes.            """ ,
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
