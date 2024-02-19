# Write code to go through all csv's in embeddings and multiply each value by 10
# Write to a new csv in the same directory with "_unscaled" appended to the name

import os
import pandas as pd

# Get the current working directory
cwd = os.getcwd()

# Get the path to the param_info directory
param_info_path = "RANCH/RANCH_cluster/sim_info/embeddings"

#iterate through all subdirectories in param_info
for root, dirs, files in os.walk(param_info_path):

    for file in files:
        if file.endswith(".csv"):
            # Get the path to the csv file
            csv_path = os.path.join(root, file)
            # Read the csv file into a pandas dataframe
            df = pd.read_csv(csv_path, header=None)
            # Multiply each numeric value in the dataframe by 10
            df = df.apply(lambda x: x*10 if x.dtype == 'float64' else x)
            # Get the name of the csv file
            file_name = os.path.basename(csv_path)
            # Get the directory of the csv file
            file_dir = os.path.dirname(csv_path)
            # Get the name of the csv file without the extension
            file_name_no_ext = os.path.splitext(file_name)[0]
            # Create a new file name with "_unscaled" appended to the original name
            new_file_name = file_name_no_ext + "_unscaled.csv"
            # Get the path to the new csv file
            new_csv_path = os.path.join(file_dir, new_file_name)
            # Write the dataframe to the new csv file
            df.to_csv(new_csv_path, index=False, header=False)
            print(f"Unscaled csv written to {new_csv_path}")