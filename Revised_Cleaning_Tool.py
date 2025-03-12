import streamlit as st
import pandas as pd
import os

def load_data(file):
    """Load CSV or Excel data into a pandas DataFrame."""
    try:
        if file.name.endswith('.csv'):
            return pd.read_csv(file)
        elif file.name.endswith('.xlsx'):
            return pd.read_excel(file)
        else:
            st.error("Unsupported file format. Please upload a CSV or Excel file.")
            return None
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

def data_report(df):
    """Generate a data quality report with a score."""
    total_cells = df.size
    missing_values = df.isnull().sum().sum()
    duplicate_rows = df.duplicated().sum()
    score = max(0, 100 - (missing_values / total_cells * 50) - (duplicate_rows / len(df) * 50))
    
    st.subheader("📊 Data Quality Report")
    st.write("- Total Rows:", len(df))
    st.write("- Total Columns:", len(df.columns))
    st.write("- Missing Values:", missing_values)
    st.write("- Duplicate Rows:", duplicate_rows)
    st.write(f"- **Data Quality Score:** {score:.2f}/100")

    #Calculate Data Quality Score
    #Data Quality Score = 100 - (Percentage of Missing Values + Errors)
    #Percentage of Missing Values = (Number of Missing Values / Total Cells) * 100 
    #Errors = (Number of Duplicate Rows / Total Rows) * 100 

def data_cleaning_tool(df):
    """Interactive data cleaning tool."""
    st.subheader("📌 Data Preview")
    if 'cleaned_df' not in st.session_state:
        st.session_state.cleaned_df = df.copy()
    
    st.dataframe(st.session_state.cleaned_df)
    
    # Remove columns
    st.subheader("🗑️ Remove Columns")
    columns_to_remove = st.multiselect("Select columns to remove", st.session_state.cleaned_df.columns)
    if st.button("Remove Selected Columns"):
        st.session_state.cleaned_df.drop(columns=columns_to_remove, inplace=True)
        st.success("Selected columns removed.")
        st.dataframe(st.session_state.cleaned_df)
    
    # Handle missing values
    st.subheader("📉 Handle Missing Values")
    missing_option = st.radio("Choose how to handle missing values:",
                              ("Remove rows with missing values", "Replace with mean", "Replace with median", "Custom value"))
    
    if missing_option == "Remove rows with missing values" and st.button("Remove Missing Rows"):
        st.session_state.cleaned_df.dropna(inplace=True)
        st.success("Rows with missing values removed.")
        st.dataframe(st.session_state.cleaned_df)
    elif missing_option == "Replace with mean" and st.button("Replace Missing Values with Mean"):
        st.session_state.cleaned_df.fillna(st.session_state.cleaned_df.mean(), inplace=True)
        st.success("Missing values replaced with mean.")
        st.dataframe(st.session_state.cleaned_df)
    elif missing_option == "Replace with median" and st.button("Replace Missing Values with Median"):
        st.session_state.cleaned_df.fillna(st.session_state.cleaned_df.median(), inplace=True)
        st.success("Missing values replaced with median.")
        st.dataframe(st.session_state.cleaned_df)
    elif missing_option == "Custom value":
        custom_value = st.text_input("Enter custom value:")
        if st.button("Replace Missing Values with Custom Value"):
            st.session_state.cleaned_df.fillna(custom_value, inplace=True)
            st.success("Missing values replaced with custom value.")
            st.dataframe(st.session_state.cleaned_df)
    
    # Change data types
    st.subheader("🔄 Change Data Types")
    column_to_change = st.selectbox("Select column to change type", st.session_state.cleaned_df.columns)
    new_type = st.selectbox("Select new type", ["int", "float", "str", "datetime"])
    if st.button("Change Data Type"):
        try:
            if new_type == "int":
                st.session_state.cleaned_df[column_to_change] = st.session_state.cleaned_df[column_to_change].astype(int)
            elif new_type == "float":
                st.session_state.cleaned_df[column_to_change] = st.session_state.cleaned_df[column_to_change].astype(float)
            elif new_type == "str":
                st.session_state.cleaned_df[column_to_change] = st.session_state.cleaned_df[column_to_change].astype(str)
            elif new_type == "datetime":
                st.session_state.cleaned_df[column_to_change] = pd.to_datetime(st.session_state.cleaned_df[column_to_change])
            st.success(f"Data type of {column_to_change} changed to {new_type}.")
            st.dataframe(st.session_state.cleaned_df)
        except Exception as e:
            st.error(f"Error changing data type: {e}")
    
    # Download cleaned dataset
    st.subheader("💾 Download Cleaned Data")
    cleaned_file = "cleaned_data.csv"
    st.session_state.cleaned_df.to_csv(cleaned_file, index=False)
    with open(cleaned_file, "rb") as f:
        st.download_button("Download Cleaned Data", f, file_name="CleanedData.csv", mime="text/csv")

def main():
    st.set_page_config(page_title="Data Processing Tool", layout="wide")
    st.title("🔍 Data Processing Tool")
    
    option = st.radio("Choose an option:", ("Data Report", "Data Cleaning Tool"))
    
    uploaded_file = st.file_uploader("📂 Upload your dataset (CSV or Excel)", type=["csv", "xlsx"])
    
    if uploaded_file is None:
        st.warning("⚠️ Please upload a file to proceed.")
        return
    
    df = load_data(uploaded_file)
    
    if df is not None:
        st.success("✅ File uploaded successfully!")
        
        if option == "Data Report":
            data_report(df)
        elif option == "Data Cleaning Tool":
            data_cleaning_tool(df)

if __name__ == "__main__":
    main()