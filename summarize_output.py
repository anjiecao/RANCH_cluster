import pandas as pd
import os

def read_and_concatenate_pickles(folder_path):
    # List all files in the folder
    all_files = os.listdir(folder_path)

    # Filter out files that are not pickle files
    pickle_files = [f for f in all_files if f.endswith('.pickle')]

    # Initialize an empty list to store DataFrames
    df_list = []

    # Loop through the pickle files and read each into a DataFrame
    for file in pickle_files:
        file_path = os.path.join(folder_path, file)
        df = pd.read_pickle(file_path)
        df_list.append(df)

    # Concatenate all DataFrames into one
    concatenated_df = pd.concat(df_list, ignore_index=True)

    return concatenated_df



# Specify the folder path containing pickle files
folder_path = 'cache_results'
all_files = os.listdir(folder_path)
# Call the function and get the concatenated DataFrame
result_df = read_and_concatenate_pickles(folder_path)

# Displaying the resulting DataFrame
print(result_df)
