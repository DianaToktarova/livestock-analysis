# Livestock Data Analysis - Kazakhstan 2024

##  Project Description
This project performs data preparation, general analysis, and basic visualization on the dataset titled **"Main indicators of livestock development in the Republic of Kazakhstan" for 2024**. The project follows steps defined in Assignment 4.2 and allows users to dynamically select any worksheet from the Excel file for analysis.

## Authors
Kim Diana, Toktarova Diana

---

##  Features
- Load and inspect any worksheet from the Excel file
- Display data structure: `head()`, `info()`, `describe()`
- Analyze and report missing values
- Clean the dataset by removing empty columns and rows
- Plot histograms and bar charts for numeric data

---

##  How to Use
1. Set your file path:
   ```python
   file_path = r"C:\Users\YourUsername\Path\livestock_kazakhstan_2024.xlsx"
   ```
2. Call the function with the desired sheet name:
   ```python
   analyze_livestock_sheet(file_path, "14.1")
   ```
   
---

## 📸 Screenshots & Explanation

### 1. Sheet Selection (`01_sheet_selection.png`)
This screenshot shows how to select the worksheet for analysis. You simply pass the sheet name (e.g., `"14.1"`) to the function.

### 2. head() Output (`02_head_output.png`)
Displays the first few rows of the dataset to get an initial overview of the structure and contents.

### 3. info() Output (`03_info_output.png`)
Provides detailed information about column data types, non-null values, and memory usage — useful for identifying missing data and formatting issues.

### 4. describe() Output (`04_describe_output.png`)
Gives basic statistical summaries of numeric data — mean, standard deviation, min, max, and quartiles.

### 5. Missing Values (`05_missing_values.png`)
Lists the number of missing values per column. Helps determine which columns may need cleaning or imputation.

### 6. Visualizations (`06_visualizations.png`)
Displays histograms and bar charts created for key numeric variables. These visualizations help in understanding the distribution and comparison of data.

---

## 📁 File Structure
```
├── livestock_kazakhstan_2024.xlsx
├── livestock_analysis.py
├── README.md
├── screenshots
│   ├── 01_sheet_selection.png
│   ├── 02_head_output.png
│   ├── 03_info_output.png
│   ├── 04_describe_output.png
│   ├── 05_missing_values.png
│   └── 06_visualizations.png
```

---

## 📖 Assignment Reference
**Assignment 4.2: Data Preparation, General Analysis, and Basic Visualization**

**Source:** [Bureau of National Statistics of Kazakhstan](https://stat.gov.kz/ru/industries/business-statistics/stat-forrest-village-hunt-fish/spreadsheets/?year=&name=18612&period=&type=)

This project covers:
- Data loading and verification
- Initial data inspection
- Missing value handling
- General exploration
- Basic data visualization

---

##  Note
You can reuse the same code to analyze any other sheet by changing only the sheet name in the function call.

