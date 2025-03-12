import pandas as pd
import argparse
from tkinter import Tk, filedialog, simpledialog
import os

def load_data(file_path):
    """Load CSV or Excel data into a pandas DataFrame."""
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Only CSV and Excel are allowed.")

def preview_data(df, num_rows=5):
    """Show a preview of the first few rows of the dataset."""
    return df.head(num_rows)

def remove_columns(df, columns_to_remove):
    """Remove the specified columns."""
    return df.drop(columns=columns_to_remove)

def filter_missing_values(df):
    """Remove rows with any missing values."""
    return df.dropna()

def replace_missing_values(df, method="mean", custom_value=None):
    """Replace missing values in the dataset."""
    if method == "mean":
        return df.fillna(df.mean())
    elif method == "median":
        return df.fillna(df.median())
    elif method == "custom" and custom_value is not None:
        return df.fillna(custom_value)
    else:
        raise ValueError("Invalid method or custom value for missing value replacement.")

def change_data_types(df, column, new_type):
    """Change the data type of a column."""
    df[column] = df[column].astype(new_type)
    return df

def save_cleaned_data(df, output_path, output_format):
    """Save the cleaned data in CSV or Excel format."""
    if output_format == "csv":
        df.to_csv(output_path, index=False)
    elif output_format == "xlsx":
        df.to_excel(output_path, index=False)
    else:
        raise ValueError("Unsupported output format. Use 'csv' or 'xlsx'.")

def interactive_cleaning(df):
    """Interactive cleaning process."""
    print("\nChoose a cleaning option:")
    print("1. Remove specific columns")
    print("2. Remove rows with missing values")
    print("3. Replace missing values")
    print("4. Change data types")
    print("5. Exit and save")
    
    while True:
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            print("\nColumns available: ", df.columns)
            columns_to_remove = input("Enter columns to remove (comma-separated): ").split(',')
            df = remove_columns(df, [col.strip() for col in columns_to_remove])
            print(f"Columns {columns_to_remove} removed.")
        
        elif choice == '2':
            df = filter_missing_values(df)
            print("Rows with missing values removed.")
        
        elif choice == '3':
            method = input("Enter replacement method (mean/median/custom): ").strip()
            if method == "custom":
                custom_value = input("Enter custom value: ").strip()
                df = replace_missing_values(df, method, custom_value)
            else:
                df = replace_missing_values(df, method)
            print("Missing values replaced.")
        
        elif choice == '4':
            column = input("Enter column name to change type: ").strip()
            new_type = input("Enter new type (int, float, str, datetime): ").strip()
            df = change_data_types(df, column, new_type)
            print(f"Data type of column {column} changed to {new_type}.")
        
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
    
    return df

def file_upload_gui():
    """GUI-based file upload using Tkinter."""
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")])
    return file_path

def main():
    # Argument parsing for command line interface
    parser = argparse.ArgumentParser(description="Interactive Dataset Cleaning Tool")
    parser.add_argument("--file", type=str, help="Path to the dataset file (CSV or Excel)", required=True)
    parser.add_argument("--output", type=str, help="Path to save the cleaned dataset", required=True)
    parser.add_argument("--format", type=str, choices=["csv", "xlsx"], help="Output format", default="csv")
    args = parser.parse_args()

    # Load dataset
    df = load_data(args.file)
    print("\nDataset Preview:\n", preview_data(df))

    # Interactive cleaning
    df = interactive_cleaning(df)
    
    # Save cleaned dataset
    save_cleaned_data(df, args.output, args.format)
    print(f"\nCleaned dataset saved to {args.output}")

if __name__ == "__main__":
    main()


##To Run This File: 'python3 data_cleaning_tool.py --file "/Users/antropravin/Desktop/Bezohminds/Task/GUI Based Data Cleaning/Uncleandata.csv" --output "/Users/antropravin/Desktop/Bezohminds/Task/GUI Based Data Cleaning/CleanedData.csv" --format csv'