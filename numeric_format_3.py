
# slip 3: Write a python program to make Categorical values in numeric format for a given dataset.

import pandas as pd

# Load the dataset from CSV file
file_path = 'your_dataset.csv'  # Replace 'your_dataset.csv' with the actual file path
df = pd.read_csv('iris.csv')

# Identify and convert categorical columns to numeric using label encoding
for column in df.select_dtypes(['object']).columns:
    df[column] = pd.factorize(df[column])[0]

# Display the transformed DataFrame
print("Transformed DataFrame:")
print(df.head())  # Display the first few rows to check the transformation

# Save the transformed DataFrame back to a CSV file
output_file_path = 'numeric_dataset.csv'  # Replace 'numeric_dataset.csv' with your desired output file name
df.to_csv(output_file_path, index=False)
print(f"Transformed data saved to {output_file_path}")