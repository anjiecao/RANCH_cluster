# Write code to go through all csv's in embeddings and multiply each value by 10
# Write to a new csv in the same directory with "_unscaled" appended to the name

import os
import pandas as pd

# Get the current working directory
cwd = os.getcwd()

# Get the path to the param_info directory
param_info_path = "RANCH/RANCH_cluster/sim_info/embeddings"

import pandas as pd

# Load the original embeddings CSV file
resnet_embeddings = pd.read_csv(os.path.join(param_info_path, 'resnet50.csv'), header=None)

# Load the second embeddings CSV file (the target range)
aligned_embeddings = pd.read_csv(os.path.join(param_info_path, 'resnet_pa.csv'), header=None)

# Assuming the first column in both is non-numeric and should be ignored for scaling
numeric_original = resnet_embeddings.iloc[:, 1:]
numeric_target = aligned_embeddings.iloc[:, 1:]

# Find the global minimum and maximum in the target embeddings
target_min = numeric_target.min().min()
target_max = numeric_target.max().max()

# Find the global minimum and maximum in the original embeddings
original_min = numeric_original.min().min()
original_max = numeric_original.max().max()

# Calculate scale factor and offset to adjust the original embeddings to the target range
scale_factor = (target_max - target_min) / (original_max - original_min)
offset = target_min - (original_min * scale_factor)

# Apply the scaling to the original numeric data
scaled_numeric_original = numeric_original * scale_factor + offset

# Combine the string descriptions with the scaled numeric data
result_df = pd.concat([resnet_embeddings.iloc[:, 0], scaled_numeric_original], axis=1)

# Write the dataframe to the new csv file
result_df.to_csv(os.path.join(param_info_path, 'resnet50_new.csv'), index=False, header=False)
print(f"Unscaled csv written to {os.path.join(param_info_path, 'resnet50.csv')}")