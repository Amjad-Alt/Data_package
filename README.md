
# Sprice - Consumer Price Data for Saudi Arabia

This data package contains two comprehensive datasets on consumer prices of 56 categories across 16 cities in Saudi Arabia, tracked monthly from 2002 to 2011 then from 2012 to 2023. Through robust and flexible cleaning pipelines, diverse data formats are standardized into a single dataset, ensuring accuracy and usability. It is designed to help analysts, economists, and policymakers analyze trends in consumer prices and inflation.method.

**Content:**   
1.Overview  
1.2 About the Data   
1.2.1 sprice_data_1   
1.2.2 sprice_data_2   
2.Methodology  
2.1 Data Processing Pipeline    
2.2 Saving  
2.3 Packaging 
3.Conclusion   
3.1 Challanges  
3.2 Limitations 
Reference      


## 1.Overview   
The Consumer Price Index (CPI) in Saudi Arabia is a comprehensive survey designed to measure the retail price fluctuations of goods and services in the consumer basket across the Kingdom. It plays a crucial role in understanding economic conditions and supporting the objectives of Vision 2030 by providing detailed statistical data on consumer prices. The data includes indices and variation rates by expenditure category, city, and time period, starting from 2002. It adheres to international standards, utilizing the Classification of Individual Consumption by Purpose (COICOP) for accurate data collection and classification. This survey is fundamental for various stakeholders, including government entities, regional organizations, and research institutions, offering insights into spending patterns and price changes essential for economic analysis and decision-making. The CPI data is available and regularly updated on the General Authority for Statistics' official website, ensuring accessibility and transparency.

### 1.2 About the Data
There are two datasets in the package, and the reason they are  divided into two is that from 2002 to 2011 they follow the same categories, then from 2012 to 2023 the categories have changed significantly that it was more suitable to have them as different datasets but follow the same structure as MultiIndex dataset.

**Table 1**

*overview of the data files included in this package*

| File Name         |Years Covered   |
|-------------------|----------------|
| `sprice_data_1.h5`| 2002 - 2011    |
| `sprice_data_2.h5`| 2012 - 2023    |

*Each dataset contains detailed consumer price indices, broken down by city, category, and month, providing a comprehensive view of consumer price trends over the specified years.*

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
*Final dataset display*
<img src="pictures/dataset_picture.png" alt="Dataset Preview" width="600"/>

*This image shows a sample of the `sprice_data_1.h5` file, illustrating the MultiIndex structure with cities, years, and months as indices.*


## 2.Methodology
The journey of developing the Sprice data processing pipelines has been both challenging and demanding. Each file format presents its own set of challenges in terms of data extraction, requiring a deep understanding of the content structure and the variations in each format. Crafting a method that is both flexible and accurate, the idea is to have a cleaning pipeline that can accept datasets in any format and structure. The pipeline is designed to handle these inputs and concatenate it with past data to ensure a consistent format across the board. Once processed, the data is then uploaded as a data package available in Python, which will be updated regularly every year following the release of new data from the Saudi General Authority for Statistics. Three stages are involved in the methodology: data preprocessing pipelines, data saving, and data packaging.

### 2.1. Data Processing Pipeline
All pipelines share a foundational approach starting with the setup of a structured multi-index DataFrame designed to categorize and store extracted data effectively. Each pipeline begins by reading files specific to its format—PDF, OCR, or Excel. It then extracts critical identifiers like month, year, city, and category through tailored techniques—ranging from regular expressions in PDFs to direct cell access in Excel. After extracting the relevant data, the pipelines match these identifiers with the extracted values and systematically insert them into the DataFrame where city, month, year, and category align. This ensures that the data across various formats is integrated cohesively and consistently for accurate analysis and reporting.

**Fig 2**   
*Multi-Source Data Extraction Methodology for each pipeline*
<img src="pictures/method.png" alt="Dataset Preview" width="600"/>

*Robust pipelines employ specialized techniques for reading, identifying, extracting, and aligning data from PDF, OCR, and Excel sources, ensuring precise integration across diverse formats*

### 2.2. Saving
HDF5 was selected for its ability to efficiently handle large volumes of complex, multidimensional data. This format supports extensive datasets with ease, offering excellent performance in both read and write operations, which is crucial for processing the intricate and extensive price index data over 22 years.

A key limitation with HDF5 is that it has restrictions on handling missing values, particularly for non-floating point data types. Therefore we used -1 as an indicate that this is a missing value. Reflecting this data structure, the `sprice_data_1.h5` dataset is approximately 1131 KB in size, while the `sprice_data_2.h5` dataset is slightly larger, approximately 1138 KB.

### 2.3. Packaging
Data comes in a clean, processed format that is ideal for immediate use in data analysis and visualization tools. Easy to use by simple installation and straightforward API make accessing data hassle-free. Additionally, instead of downloading new data each time it is updated, users can conveniently upgrade the package with a simple update command, ensuring they always have the latest information.

**Installation**   
To install sprice, simply run the following command:

```bash
pip install sprice
```
After installation, the data can be loaded into a Python environment using:

```python
import sprice
data1 = sprice.sprice_data_1
data2 = sprice.sprice_data_2

print(data1.head())
print(data2.head())
```   
Each year, as new data for the past year is added to the package, ensure you keep your version updated by running:
```bash
pip install --upgrade sprice
```
## 3. Conclusion
The Sprice project significantly enhances the accessibility and usability of consumer price data across Saudi Arabia. By consolidating complex and varied data into a streamlined, easy-to-use package, it empowers analysts, economists, and policymakers to effectively track and analyze inflation and pricing trends. This project not only supports informed decision-making and economic planning but also contributes to the broader understanding of economic dynamics. The ongoing updates ensure that the data remains relevant, providing a valuable tool for continuous improvement in economic strategies and consumer insight. Ultimately, Sprice helps to foster a deeper understanding of economic conditions, facilitating a more informed and proactive approach to both regional and global economic challenges.   
### 3.1 Challenges
There were many obstacles along the way, every file format has a different process of extracting the data and it was challenging to navigate through the data to figure out a method that is flexible to all files yet accurate. It is important to understand the data and how it is displayed yet there are always things that come up on the way like different city spelling, different category names but the same meaning, sudden different indexing, empty rows and columns, unorganized structure of the data, etc. The hardest part is to find a foundation that all the 22 years stand on. Then organize them into groups based on the data format and how it is displayed, and create a solid pipeline for each group that considers the small variations within each file. 

### 3.2 Limitations
Despite the robustness of the Sprice data processing pipelines, certain limitations have emerged. Notably, in the year 2020, data for January is missing because the pipeline struggled to adapt to the significantly different data structure presented that month, and attempts to modify the method led to a collapse in the process. Additionally, from 2012 to 2014, there are gaps in the data for categories such as miscellaneous goods and services, pre-primary & primary education, secondary & intermediate education, recreational & cultural services, other recreation & culture goods, telephone and telefax equipment, telephone and telefax services, operation of transport equipment, goods for household maintenance, furniture & carpets, furnishings, household equipment and maintenance, and housing, water, electricity, gas and other fuels. This was due to the challenge of processing scanned documents where categories written over two lines were not recognized as a single entry by the reading tools.

## References    
### Data Source
General Authority for Statistics. (n.d.). Consumer Price Indices. Retrieved January 3, 2024, from https://www.stats.gov.sa/en/394

### License
Sprice is released under the MIT license. Please see the LICENSE file for more details.