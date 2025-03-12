# GUI-Based-Data-Cleaning
### Overview
The Data Cleaning Tool provides two different ways to clean and preprocess datasets:

1. **Streamlit-based Interactive Web App** - A user-friendly interface for data cleaning and reporting.

2. **Command Line Interface (CLI) Tool** - A terminal-based interactive tool for cleaning datasets.

Both tools support CSV and Excel file formats and provide functionalities such as removing columns, handling missing values, changing data types, and generating data reports.

# Features
## Streamlit-based Web App

**Data Report:**

* Analyzes the dataset and provides a quality score (0-100)

* Reports total rows, columns, missing values, and duplicate rows

**Data Cleaning Tool:**

* Remove unwanted columns

* Handle missing values (remove rows, replace with mean/median/custom values)

* Change data types (int, float, string, datetime)

* Download the cleaned dataset

**CLI-based Data Cleaning Tool**

* Loads a dataset from a CSV or Excel file

* Provides an interactive menu for cleaning operations:

    * Remove specific columns
    *Remove rows with missing values
    *Replace missing values with mean/median/custom value
    *Change data types of columns

* Saves the cleaned dataset in CSV or Excel format

### Installation

1. Clone the repository:
```bash
git clone https://github.com/antrovibin/data-cleaning-tool.git
cd data-cleaning-tool
```

# Usage
## Running the Streamlit Web App

1. Run the following command in the project directory:
```bash
streamlit run streamlit_data_cleaning.py
This will open the web-based interface in your browser, allowing you to upload and clean datasets.
```

2. Running the CLI-based Tool
Use the following command to clean a dataset using the terminal:
```bash
python3 data_cleaning_tool.py --file "/path/to/input.csv" --output "/path/to/output.csv" --format csv
```

Example:
```bash
python3 data_cleaning_tool.py --file "./data/uncleaned.csv" --output "./data/cleaned.csv" --format csv
```

# Dependencies
Dependencies

1. Python 3.x

2. Libraries:

   * pandas
   * streamlit
   * argparse
   * tkinter

