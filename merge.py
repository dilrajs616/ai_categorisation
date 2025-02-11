import pandas as pd

# Load the CSV files
categories_df = pd.read_csv('output.csv')
test_domains_df = pd.read_csv('sample_dataset.csv')

# Keep only the 'sector' and 'industry' columns from the second CSV
test_domains_df = test_domains_df[['website', 'sector', 'industry']]

# Merge the dataframes based on 'url' from categories.csv and 'website' from test_domains.csv
merged_df = pd.merge(categories_df, test_domains_df, left_on='URL', right_on='website', how='left')

# Drop the 'website' column to avoid duplication
merged_df = merged_df.drop(columns=['website'])

# Save the merged result into a new CSV file
merged_df.to_csv('llama3_1output.csv', index=False)

print(f'Merged file created with {len(merged_df)} rows and the columns: {list(merged_df.columns)}')
