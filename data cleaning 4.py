import pandas as pd

# Load the CSV file
file_path = 'C:\Alloveww-Project\Profolio\Dashboards\EN_APEI-Can-Prov_Terr.csv'
data = pd.read_csv(file_path)

# Replace "CA" and "Unspecified" with a single new category
data['Region'] = data['Region'].replace({'CA': 'Unknown Region', 'Unspecified': 'Unknown Region'})

# Save the cleaned data to a new CSV file
cleaned_file_path = 'C:\Alloveww-Project\Profolio\Dashboards\cleaned_EN_APEI-Can-Prov_Terr.csv'
data.to_csv(cleaned_file_path, index=False)

# Print all distinct regions to verify
distinct_regions = data['Region'].unique()
print(distinct_regions)

# Verify the new data with coordinates
print(data.head())
