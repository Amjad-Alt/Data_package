
# Sprice - Consumer Price Data for Saudi Arabia

This data package contains two comprehensive datasets on consumer prices in 56 categories across 16 cities in Saudi Arabia, tracked monthly from 2002 to 2011 then from 2012 to 2023. It is designed to help analysts, economists, and policymakers analyze trends in consumer prices and inflation.

**Content:**
1.Pacakge Content  
1.2 About the Data   
1.2.1 sprice_data_1   
1.2.2 sprice_data_2   
2.Methodology  
2.1. Data Processing Pipeline    
2.2. Saving   
2.3. Challanges  
Reference      


## 1.Pacakge Content

There are two datasets in the package, and the reason they are devides into two is that from 2002 to 2011 they follow the same categories, then from 2012 to 2023 the categories have changed significantly that it was more suitable to have them as different datasets but follow the same structure as MultiIndex dataset.

**Table 1**

*overview of the data files included in this package*

| File Name         |Years Covered   |
|-------------------|----------------|
| `sprice_data_1.h5`| 2002 - 2011    |
| `sprice_data_2.h5`| 2012 - 2023    |

*Each dataset contains detailed consumer price indices, broken down by city, category, and month, providing a comprehensive view of consumer price trends over the specified years.*

### 1.2 About the Data
**1.2.1 sprice_data_1**
- Years: 2002 to 2011 `integer`
- Months: the 12 months `string`
- Cities: 16 cities (Riyadh, Makkah, Jeddah, Dammam, Tiaf, Medina, Abha, Alhofof, Tabuk, Buraydah, Jazzan, Hail, Njran, Baha, Skaka and Arar) `string`
- Categories (each as a standing column): General Index, Foodstuffs, Cereals and cereal products, Meat and Poultry, Fish and crustaceans, Milk and dairy products, Eggs, Cooking oil and fats, Fresh vegetables, Preserved and canned vegetables, Legumes and tubers, Fresh fruits, Preserved and canned fruits, Nuts, peanuts, seeds, Sugars and sugar preparations, Beverages, Foodstuffs, other, Tobacco, Out-of-home meals, Fabrics, clothing and footwear, Men's fabrics, Women's fabrics, Men's apparel, Women's apparel, Tailoring, Footwear, House and related items, Home repairs, Rents, Water supply expenditure, Fuel and Power, Home furniture, Furniture and carpet, Home furnishings, Small home appliances, kitchenhouse & tabletualis, Household small items, Home services, Basic home appliances, Medical care, Medical care expenses, Other medical expenses, Medicines, Transport and telecommunications, Private transport means, Operation of private transport means, Public transport fees, Telecommunications and related costs, Education and entertainment, Entertainment expenses, Education expenses, Entertainment devices, Other expenses and services, Personal hygiene and care items, Personal goods, Other expenses and services. `float`

**1.2.2 sprice_data_2**
- Years: 2012 to 2023 `integer`
- Months: the 12 months `string`
- Cities: 16 cities (Riyadh, Makkah, Jeddah, Dammam, Tiaf, Medina, Abha, Alhofof, Tabuk, Buraydah, Jazzan, Hail, Njran, Baha, Skaka and Arar) `string`
- Categories (each as a standing column): General Index, FOOD AND BEVERAGES, FOOD, BEVERAGES, TOBACCO, CLOTHING AND FOOTWEAR, CLOTHING, FOOTWEAR, HOUSING, WATER, ELECTRI-CITY ,GAS AND OTHER FUELS, RENTALS FOR HOUSING, MAITENANCE OF THE DEWELLING, WATER SUPPLY & OTHER SERVICES, ELECTRICITY, GAS AND OTHER FUELS, FURNISHINGS, HOUSEHOLD EQUIPMENT AND MAINTENANCE, FURNITURE & CARPETS, HOUSEHOLD TEXTILES, HOUSEHOLD APPLIANCES, HOUSEHOLD UTENSILS, TOOLS FOR HOUSE & GARDEN, GOODS FOR HOUSEHOLD MAINTENANCE, HEALTH, MEDICAL PRODUCTS & EQUIPMENT, OUTPATIENT SERVICES, HOSPITAL SERVICES, TRANSPORT, PURCHASE OF VEHICLES, OPERATION OF TRANSPORT EQUIPMENT, TRANSPORT SERVICES, COMMUNICATION, POSTAL SERVICES, TELEPHONE AND TELEFAX EQUIPMENT, TELEPHONE AND TELEFAX SERVICES, RECREATION AND CULTURE, AUDIO, PHOTO & INFO. EQUIPMENT, OTHER RECREATION & CULTURE GOODS, OTHER RECREATIONAL GOODS, RECREATIONAL & CULTURAL SERVICES, NEWSPAPERS, BOOKS & STATIONERY, PACKAGE HOLIDAYS, EDUCATION, PRE-PRIMARY & PRIMARY EDUCATION, SECONDARY&INTERMEDIATE EDUCATION, POST-SECONDARY EDUCATION, TERTIARY EDUCATION, RESTAURANTS AND HOTELS, CATERING SERVICE, ACCOMMODATION SERVICES, MISCELLANEOUS GOODS AND SERVICES, PERSONAL CARE, PERSONAL EFFECTS N.E.C., SOCIAL PROTECTION, INSURANCE, FINANCIAL SERVICES N.E C., OTHER SERVICES N.E.C. `float`

**Fig 1**
*Final dataset displayed*
<img src="pictures/dataset_picture.png" alt="Dataset Preview" width="600"/>

*This image shows a sample of the `sprice_data_1.h5` file, illustrating the MultiIndex structure with cities, years, and months as indices.*


## 2.Methodology

The journey of developing the Sprice data processing pipelines has been both intricate and demanding. Each file format presents its own set of challenges in terms of data extraction, necessitating a deep understanding of the content structure and the nuances inherent in each format. Crafting a method that is both flexible and accurate across all file types required significant innovation and perseverance. the methodolgy goes in three stages; first data preprosessing pipelines, then data saving and data packaging.

### 2.1. Data Processing Pipeline

There are four pipelines for each file structure, including PDFs, scanned files, Excel xlxs, and Excel csv. The cores are the same, but the details are different due to the different nature of the displayed data and how the information should be extracted.

The base core of the processing system: function to read the data from the file > function to extract the page needed by checking unique text > function to extract the month, the year, and the city> function to extract the category name and it's values > function to mach the category and the value to its year, month, and city.

**Fig 2**

### 2.2. Saving

HDF5 was selected for its ability to efficiently handle large volumes of complex, multidimensional data. This format supports extensive datasets with ease, offering excellent performance in both read and write operations, which is crucial for processing the intricate and extensive price index data over 22 years.

A key limitation with HDF5 is that it has restrictions on handling missing values, particularly for non-floating point data types. Therefore we used -1 as an indicate that this is a missing value. 

### 2.3. Challanges

every file format has a different process of extracting the data and it was challenging to navigate through the data to figure out a method that is flexible to all files yet accurate. It is important to understand the data and how it is displayed yet there are always things that come up on the way like different city spelling, different category names but the same meaning, sudden different indexing, empty rows and columns, unorganized structure of the data, etc. The hardest part is to find a foundation that all the 22 years stand on. Then organize them into groups based on the data format and how it is displayed, and create a solid pipeline for each group that considers the small variations within each file. 

## References    
### Data Source
Data collected from here: https://www.stats.gov.sa/en/394
