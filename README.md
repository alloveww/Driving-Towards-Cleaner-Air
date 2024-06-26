﻿# EV Adoption and Emission Trends in Canada

## Overview

This repository contains the code for analyzing the impact of government incentives on the adoption of electric vehicles (EVs) and emission trends in Canada. The folder includes data cleaning and preparation steps using pandas.

## Contents

- `data_cleaning.py`: Python script for cleaning and preparing the data using pandas.
- `data/`: Directory containing the datasets used in the analysis.
- `visualizations/`: Directory with visualizations generated from the analysis.
- `README.md`: This file, providing an overview of the repository.

## Data Cleaning

The `data_cleaning.py` script includes the following steps:
- Loading datasets into pandas dataframes.
- Handling missing values by either dropping them or grouping them under "unspecified" if the specific province is not determinable.
- Ensuring all data types are correctly formatted.
- Unifying column names and ensuring consistent terminology.
- Filtering to select only the required data columns.
- Merging datasets based on common terms.
- Grouping different types of EVs (Battery Electric Vehicles, Hybrid Electric Vehicles, and Plug-in Hybrid Electric Vehicles) into a single category labeled as "EVs".
- Combining data for northern territories with British Columbia and its territories due to the low number of EV sales in northern regions.

