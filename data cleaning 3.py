import pandas as pd

# Load the dataset
file_path = 'C:/Alloveww-Project/Profolio/Dashboards/Cleaner Air/EV Incentives in Canada 2017-2023.csv'
incentives = pd.read_csv(file_path)

# Combine the provinces into "British Columbia and the Territories"
bc_territories = ['British Columbia', 'Yukon', 'Northwest Territories','Nunavut']
incentives['GEO'] = incentives['Province'].replace(bc_territories, 'British Columbia and the Territories')

# Drop the old 'Province' column
incentives.drop(columns=['Province'], inplace=True)

# Save the modified DataFrame to a new CSV file
cleaned_file_path = 'C:/Alloveww-Project/Profolio/Dashboards/Cleaner Air/cleaned_provincial_and_federal_ev_incentives_2017_2023.csv'
incentives.to_csv(cleaned_file_path, index=False)

print("The file has been cleaned and saved successfully.")
