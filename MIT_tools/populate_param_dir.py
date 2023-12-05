
def populate_dir(args):

# first empty param dir

    # read csv
    pd.read_csv('')


# get one row and create csv in param_dir




if __name__ == '__main__':
    print('entered main script')
    parser = argparse.ArgumentParser()
    parser.add_argument("param_info_path", type=str, help="Path to csv with parameters")
    args = parser.parse_args()
    populate_dir(args)