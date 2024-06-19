import pandas as pd

# Load the dataset
file_path = 'C:/Alloveww-Project/Profolio/Dashboards/Cleaner Air/2010002402_databaseLoadingData.csv'
data = pd.read_csv(file_path)

# Display the first few rows to understand the structure
print("First few rows of the dataset:")
print(data.head())

# Check for missing values
print("\nMissing values in each column:")
print(data.isnull().sum())

# Drop rows with missing values
data_cleaned = data.dropna(subset=['VALUE'])

# Select relevant columns
selected_columns = data_cleaned[['REF_DATE', 'GEO', 'Fuel type', 'Vehicle type', 'VALUE']]

# Save the cleaned data to a new CSV file
cleaned_file_path = 'C:/Alloveww-Project/Profolio/Dashboards/Cleaner Air/cleaned_provincial_ev_sales.csv'
selected_columns.to_csv(cleaned_file_path, index=False)

print("\nData cleaning complete. Cleaned data saved to:", cleaned_file_path)
print("First few rows of the cleaned data:")
print(selected_columns.head())
