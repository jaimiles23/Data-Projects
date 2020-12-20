"""
Module to import relevant data
"""

##########
# Imports
##########

import os
from typing import Tuple

import pandas as pd


##########
# Constants
##########

## Urls to download csvs
url_info_csv = 'https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons.csv'
url_email_csv = 'https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons_email.csv'
url_sub_csv = 'https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons_email_chapter_subscription.csv'

url_csvs = (
    url_info_csv,
    url_email_csv,
    url_sub_csv
)

## Csv file names
csv_datafiles = (
    'cons.csv',      ## info
    'cons_email.csv',                      
    'cons_email_chapter_subscription.csv'   
)

##########
# Load_df
##########

def load_df(filename_csv: str, url_csv: str) -> object:
    """Auxiliary function to load csvs into dataframe.
    
    Checks if csv exists in working directory. 
    If not, downloads csv from url.
    """
    file_path = f'./{filename_csv}'
    
    print('\n', '#' * 5, ' ',  filename_csv, sep = '')
    if os.path.isfile(file_path):
        print("Reading from working directory.")
        df = pd.read_csv(filename_csv)
    
    else:
        print("Loading data from url. This is a large file, so please be patient.")
        df = pd.read_csv(url_csv)
        
        print(f"\tSaving {filename_csv} to working directory.")
        df.to_csv(path_or_buf = filename_csv)
    
    print(f"""Loaded df for {filename_csv}:
    - {len(df.columns)} columns
    - {len(df)} rows""")
    return df


##########
# Get data frames
##########

def get_data() -> Tuple[object, object, object]:
    """Returns df_info, df_emails, df_subs, and all_cons_dfs"""
    df_info, df_emails, df_subs = (
        load_df(csv_datafiles[i], url_csvs[i]) for i in range(len(csv_datafiles))
        )

    print("\nLoaded all csv data.")
    return (df_info, df_emails, df_subs)

