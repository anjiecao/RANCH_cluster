import pandas as pd
import os
import ipdb
import argparse 

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

        ipdb.set_trace()
        
        # summarize df by taking mean and std of n_samples, while retaining the other columns
        df = df.reset_index()
        df = df.groupby(['trial_id', 'stim_id', 'param_id', 'index']).agg({'sample_n': ['mean', 'std']})

        df.columns = ['_'.join(col).strip() for col in df.columns.values]
        df = df.reset_index()

        df_list.append(df)

    # Concatenate all DataFrames into one
    concatenated_df = pd.concat(df_list, ignore_index=True)

    return concatenated_df

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_folder_path", type=str, help="Path to sim results")
    parser.add_argument("output_path", type=str, help="Path to sim results")
    args = parser.parse_args()    
    result_df = read_and_concatenate_pickles(args.input_folder_path)
    result_df.to_csv(args.output_path, index=False)
