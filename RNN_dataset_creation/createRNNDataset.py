import pandas as pd

# Load the datasets
justPSMwsamyus_dataset = pd.read_csv('./justPSMwsamyus_dataset.csv')
samyus_cleaned_dataset = pd.read_csv('./samyus_cleaned_dataset.csv')

# Ensure the common columns are consistent in both datasets before merging
# Assuming 'cDNA' column is the key for merging. Adjust if necessary.
merged_dataset = pd.merge(justPSMwsamyus_dataset, 
                          samyus_cleaned_dataset[['cDNA', 'seqBefore', 'seqAfter']], 
                          on='cDNA', 
                          how='left')

# Save the merged dataset
merged_dataset.to_csv('RNN_dataset.csv', index=False)

print("RNN_dataset.csv has been created successfully.")
