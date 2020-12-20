"""
Script to run ALS_DataEngineer_Assessment exercises and produce 2 output files:
    1. people.csv
    2. acquisition_facts.csv

Contains 3 sections:
    - Imports
    - Constants, which were previously identified as relevant in the jupyternb EDA
    - Main script

Main runs the following steps:
    - Get data
    - Data Wrangling I
        - Keep relevant columns
        - Fix missing data
    - Clean strings
    - Data Wrangling II
        - Remove duplicates
        - Clean datetime
        - Join data
    - People.csv
        - Select data
        - Set rows and columns
        - Fill Missing data
        - Write to csv
    - Acquisition_facts.csv
        - Create acquired column
        - Group by acquired
        - write to csv

Method documentation available in ETL Documentation.md
"""

##########
# Imports
##########

import os
import re
from typing import List, Tuple

import numpy as np
import pandas as pd
import pywrangle as pw  # streamline data wrangling.

from script import date_funcs, duplicates, import_data, join_dfs, relevant_data
from script.header import print_header

pd.options.mode.chained_assignment = None  # default='warn' - disables false positive warnings


##########
# Constants
##########

## Relevant columns in each data frame.
COLS_DF_INFO = [
    'cons_id',
    'source',
    'create_dt',
    'modified_dt'
]
COLS_DF_EMAIL = [
    'cons_email_id',
    'cons_id',
    'email',
]
COLS_DF_SUBS = [
    'cons_email_chapter_subscription_id',
    'cons_email_id',
    'isunsub'
]

## Missing data in each df 
# NOTE: Missing data was identified in EDA in jupyter nb
MISSING_DF_INFO = (
    'source', 
)
MISSING_FILL = "unknown"

## String cleaning
# NOTE: Use pywrangle to standardize string column casing. 
# Pass a tuple of tuples containing a string indicating the column to clean, and an integer representing the cleaning method to use.
CONS_INFO_STRCOL_CASEINT: Tuple[ Tuple[ str, int]] = (
    ("source", 0),
    ("create_dt", 0),
    ("modified_dt", 0)
)
CONS_EMAIL_STRCOL_CASEINT: Tuple[ Tuple[ str, int]] = (
    ('email', 0),
)

## Duplicates
# NOTE: Identified duplicates in foreign key of df_subs in EDA
DUP_SUBS_COL = 'cons_email_id'


## Datetime
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
DATETIME_DF_INFO_COLS = ('create_dt', 'modified_dt')


## People file constants
COLS_USE_FOR_PEOPLE = [
    'email',
    'source',
    'isunsub',
    'create_dt',
    'modified_dt'
]
PEOPLE_COLNAMES = (
    'email',
    'code',
    'is_unsub',
    'created_dt',
    'updated_dt'
)
Q1_FILENAME = 'people.csv'

## Acquisition_facts file constants
Q2_FILENAME = "acquisition_facts.csv"
ACQUISITION_GROUP_VAR = ['acquired']

## Script info
SCRIPT_INFO = f"""This script creates solutions to the ALS Hiring Data Engineer Exercise.

It creates two csv files in the current working directory:
- {Q1_FILENAME}
- {Q2_FILENAME}

Steps taken are documented on the terminal during run-time.

Please note: This script may also download the input data to the current working directory.
"""


##########
# Main
##########

def main():
    """
    Main function runs ETL script for ALS Exercises:
        - Get data
        - Data Wrangling I
            - Keep relevant columns
            - Fix missing data
        - Clean strings
        - Data Wrangling II
            - Remove duplicates
            - Clean datetime
            - Join data
        - People.csv
            - Select data
            - Set rows and columns
            - Fill Missing data
            - Write to csv
        - Acquisition_facts.csv
            - Create acquired column
            - Group by acquired
            - write to csv
    
    NOTE: Clean strings has its own section to increase clarity of output print statements
    """
    print_header("Script info")
    print(SCRIPT_INFO)

    ## Get Data
    print_header("Get Data")
    df_info, df_emails, df_subs = import_data.get_data()

    ##### Wrangling 1
    print_header("Wrangling")

    ## Keep relevant columns
    print("- Keeping relevant columns")
    df_cols: Tuple[tuple] = (
        (df_info, COLS_DF_INFO),
        (df_emails, COLS_DF_EMAIL),
        (df_subs, COLS_DF_SUBS)
    )
    df_info, df_emails, df_subs = (
        relevant_data.keep_df_cols(df_cols[i][0], df_cols[i][1]) for i in range(len(df_cols))
    )

    ## Fix missing data. identified in EDA of jupyter nb
    print("- Filling misisng data")
    for data in MISSING_DF_INFO:
        df_info[data].fillna(MISSING_FILL, inplace = True)

    ## Clean string data
    print_header("Cleaning strings")
    df_info = pw.clean_str_columns( df_info, CONS_INFO_STRCOL_CASEINT)
    df_emails = pw.clean_str_columns( df_emails, CONS_EMAIL_STRCOL_CASEINT)

    ##### Wrangling 2
    print_header("Data Wrangling 2")

    ## Remove duplicates
    print("- Removing Duplicates")
    df_subs = duplicates.remove_df_duplicates(df_subs, DUP_SUBS_COL, keep = False)

    ## Clean datetime
    print("- Cleaning datetime")
    for col in DATETIME_DF_INFO_COLS:
        df_info[col] = df_info[col].map( date_funcs.get_datetime)
        df_info[col] = pd.to_datetime(df_info[col], format = DATETIME_FORMAT)
    
    ## Join data
    print("- Joining data")
    df_email_info_subs = join_dfs.get_total_df(df_emails, df_info, df_subs)
    
    ##### People.csv
    print_header(f"Creating {Q1_FILENAME}")
    print("- Selecting data")
    df_q1 = df_email_info_subs[ COLS_USE_FOR_PEOPLE]

    print("- Setting rows and columns")
    df_q1.reset_index(drop = True, inplace = True)
    df_q1.columns = PEOPLE_COLNAMES

    ## Fill missing data from merge
    print("- Filling missing columns")
    dfq1_missing_col = 'is_unsub'
    df_q1[dfq1_missing_col].fillna(MISSING_FILL, inplace = True)

    ## Output people file
    print(f'- Saving {Q1_FILENAME}. Please be patient.')
    df_q1.to_csv( path_or_buf = Q1_FILENAME, index = False)
    print(f"- Wrote dataframe to {Q1_FILENAME}")

    
    ##### Q2: Acquisition Facts
    print_header(f"Creating {Q2_FILENAME}")
    print('- Creating acquired column')
    df_q1['acquired'] = df_q1['created_dt'].dt.date

    print('- Grouping by acquired')
    df_q2 = (
        df_q1
        .groupby( ACQUISITION_GROUP_VAR, as_index = True)
        .count()
        .sort_values(ACQUISITION_GROUP_VAR, ascending = True)['email']
        .reset_index()
    )

    print(f'- Saving {Q2_FILENAME}')
    df_q2.to_csv(
        path_or_buf = Q2_FILENAME,
        index = False
    )
    print(f"- Wrote dataframe to {Q2_FILENAME}")


    ## Allow user to read script notes.
    input("\n\nPress enter to exit")


##########
# If Main
##########

if __name__ == "__main__":
    main()

