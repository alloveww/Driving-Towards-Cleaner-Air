import pandas as pd

# Load the new dataset
file_path = r'C:\Alloveww-Project\Profolio\Dashboards\Cleaner Air\2310030801_databaseLoadingData.csv'
vehicle_registrations = pd.read_csv(file_path)

# Display the first few rows and column names of the new dataset
print(vehicle_registrations.head())
print(vehicle_registrations.columns)

# Inspect the data types and look for missing values
print(vehicle_registrations.info())
print(vehicle_registrations.isnull().sum())

# Filter relevant columns
# Assume we only need columns: 'DATE', 'GEO', 'Vehicle Type', 'Fuel Type', 'VALUE'
filtered_data = vehicle_registrations[['REF_DATE', 'GEO', 'Vehicle Type', 'Fuel Type', 'VALUE']]
bc_territories = ['British Columbia', 'Yukon', 'Northwest Territories','Nunavut']
filtered_data['GEO_Final'] = filtered_data['GEO'].replace(bc_territories, 'British Columbia and the Territories')

# Handle missing values, e.g., drop rows with missing values
cleaned_data = filtered_data.dropna()

# Convert data types if needed
# Example: cleaned_data['DATE'] = cleaned_data['DATE'].astype(int)
# Convert 'VALUE' to integer
cleaned_data['VALUE'] = cleaned_data['VALUE'].astype(int)

# Save the cleaned data to a new CSV file
cleaned_file_path = r'C:\Alloveww-Project\Profolio\Dashboards\Cleaner Air\cleaned_vehicle_registrations.csv'
cleaned_data.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data saved to {cleaned_file_path}")

# Display the first few rows of the cleaned data
print(cleaned_data.head())
