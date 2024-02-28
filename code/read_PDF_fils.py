
import fitz
import pandas as pd
import re


def extract_text_from_pdf(pdf_path, page_numbers):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in page_numbers:
        # Check if the page number is valid
        if page_num < len(doc):
            text += doc[page_num].get_text()
    return text


[10, 11, 12, 13, 14, 15, 16, 17]  # Jan and Feb
[] # Mar and Apr
[116,117,118,119,120,121,122,123] # May and Jun
[154, 155, 156, 157, 158, 159, 160, 161] # July and Aug
[192, 193, 194, 195, 196, 197, 198, 199]  # Sep and Oct
[230, 231, 232, 233, 234, 235, 236, 237]  # Nov and Dec

pages_to_extract = [192, 193, 194, 195, 196, 197, 198, 199]  # sep and oct


def parse_text_to_data(text):
    # Delete non-English characters
    text = re.sub(r'[^a-zA-Z0-9\s,.]', '', text)
    cleaned_text = re.sub(r'[a-zA-Z\u0600-\u06FF]', '', text)
    
    # we need to swich all the numbers into English
    # Split the cleaned text into lines or comma-separated values
    elements = re.split(r'[\n,]+', cleaned_text.strip())

    strings_to_remove = [
        '99100',
        '2002',
    ]

    # Remove specified strings from each element
    for remove_string in strings_to_remove:
        elements = [element.replace(remove_string, '') for element in elements]

    # Delete numbers '19', '4'
    elements = [re.sub(r'\b(?:19|(?<![\d.])4\b(?![\d.]))', '', element)
                for element in elements]

    # Filter out empty elements and elements containing only periods (with flexible length)
    filtered_elements = [element for element in elements if element.strip(
    ) and not re.fullmatch(r'\.+', element.strip())]

    # Group filtered elements into rows with # of elements each
    rows = [filtered_elements[i:i+56]
            for i in range(0, len(filtered_elements), 56)]

    # Delete every third row after every two rows
    rows = [row for i, row in enumerate(rows) if i % 3 != 2]
    return rows


def create_csv_from_data(data, csv_path, column_names):
    df = pd.DataFrame(data, columns=column_names)
    df.to_csv(csv_path, index=False)


# Update with the path to your PDF
pdf_path = '/Users/amjad/OneDrive/المستندات/GWU_Cources/Spring2024/capstone_project/data/2002.pdf'
# Update with your desired CSV path
csv_path = '/Users/amjad/OneDrive/المستندات/GWU_Cources/Spring2024/capstone_project/code/output2.csv'

text = extract_text_from_pdf(pdf_path, pages_to_extract)
data = parse_text_to_data(text)

# column names
column_names = ['General Index',
                'Foodstuffs',
                'Cereals and cereal products',
                'Meat and Poultry',
                'Fish and crustaceans',
                'Milk and dairy products',
                'Eggs',
                'Cooking oil and fats',
                'Fresh vegetables',
                'Preserved and canned vegetables',
                'Legumes and tubers',
                'Fresh fruits',
                'Preserved and canned fruits',
                'Nuts, peanuts, seeds',
                'Sugars and sugar preparations',
                'Beverages',
                'Foodstuffs, other',
                'Tobacco',
                'Out-of-home meals',
                'Fabrics, clothing and footwear',
                'Mens fabrics',
                'Womens fabrics',
                'Mens apparel',
                'Womens apparel',
                'Tailoring',
                'Footwear',
                'House and related items',
                'Home repairs',
                'Rents',
                'Water supply expenditure',
                'Fuel and Power',
                'Home furniture',
                'Furniture and carpet',
                'Home furnishings',
                'Small home appliances',
                'kitchenhouse & tabletualis',
                'Household small items',
                'Home services',
                'Basic home appliances',
                'Medical care',
                'Medical care expenses',
                'Other medical expenses',
                'Medicines',
                'Transport and telecommunications',
                'Private transport means',
                'Operation of private transport means',
                'Public transport fees',
                'Telecommunications and related costs',
                'Education and entertainment',
                'Entertainment expenses',
                'Education expenses',
                'Entertainment devices',
                'Other expenses and services',
                'Personal hygiene and care items',
                'Personal goods',
                'Other expenses and services'
                ]
create_csv_from_data(data, csv_path, column_names)
