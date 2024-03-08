import fitz  # PyMuPDF


def extract_pages_with_word(pdf_path, word):
    # Open the PDF file
    doc = fitz.open(pdf_path)
    adjusted_pages_with_word = []
    word_found_counter = 0  # Initialize a counter for occurrences of the word

    # Iterate through each page in the document
    for page_num in range(len(doc)):
        # Extract text from the current page
        page_text = doc[page_num].get_text()

        # Check if the word is in the current page's text, case-insensitive search
        if word.lower() in page_text.lower():
            # Increment the counter each time the word is found
            word_found_counter += 1

            # Include the page number (0-indexed) if this is the second or any subsequent even occurrence of the word
            if word_found_counter % 2 == 0:
                # Keeping it 0-indexed as per your request
                adjusted_pages_with_word.append(page_num)

    return adjusted_pages_with_word


# Path to the PDF file
pdf_path = "/Users/amjad/OneDrive/المستندات/GWU_Cources/Spring2024/capstone_project/data/2003.pdf"
word = "MAKKAH"

# Except if the file name is 2002 then skip the first two MAKKAH and get the page number with the third apperance
# Find pages containing the specified word
pages_with_makkah = extract_pages_with_word(pdf_path, word)
pages_with_makkah

# from 2012 the name of columns change
# you can't specify the name of cities in a loop coz it can be in different order in term of pages
# we can have more than one data like there is the month/year 