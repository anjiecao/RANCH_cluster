import pandas as pd
import os
import ipdb
import argparse 

def read_and_concatenate_pickles(folder_path, output_path):
    # List all files in the folder
    all_files = os.listdir(folder_path)

    # Filter out files that are not pickle files
    pickle_files = [f for f in all_files if f.endswith('.pickle')]

    # Initialize an empty list to store DataFrames
    df_list = []  # Initialize the list to store data frames

    for idx, file in enumerate(pickle_files):
        file_path = os.path.join(folder_path, file)
        df = pd.read_pickle(file_path)
        
        # Reset index and perform group by operation
        df = df.reset_index()
        df = df.groupby(['trial_id', 'stim_id', 'param_id', 'index']).agg({'sample_n': ['mean', 'std']})
        df.columns = ['_'.join(col).strip() for col in df.columns.values]  # Flatten the column headers
        df = df.reset_index()
        df_list.append(df)

        if (idx + 1) % 200 == 0:  # Check if the current index + 1 is divisible by 200
            print(f"Processed {idx + 1} files")
            concatenated_df = pd.concat(df_list, ignore_index=True)
            if not os.path.isfile(output_path):
                concatenated_df.to_csv(output_path, header='column_names', index=False)
            else:
                concatenated_df.to_csv(output_path, index=False, mode='a', header=False)
            df_list = []  # Reset the list after writing to file

    # After the loop, check if there are any remaining data frames to write to the file
    if df_list:
        concatenated_df = pd.concat(df_list, ignore_index=True)
        if not os.path.isfile(output_path):
            concatenated_df.to_csv(output_path, header='column_names', index=False)
        else:
            concatenated_df.to_csv(output_path, index=False, mode='a', header=False)

    return concatenated_df

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_folder_path", type=str, help="Path to sim results")
    parser.add_argument("output_path", type=str, help="Path to sim results")
    args = parser.parse_args()    
    result_df = read_and_concatenate_pickles(args.input_folder_path, args.output_path)
    
