"""
Script to merge df_emails, df_info, and df_subs into one dataframe for the people.csv output
"""

##########
# Imports
##########

import pandas as pd 


##########
# Join dataframes
##########

def get_total_df(df_emails: object, df_info: object, df_subs: object) -> "dataframe":
    """Returns dataframe of input constituent data merged on relational keys.

    Check methods documentation in readme.md
    """
    # Left Join df_emails and df_info
    df_email_info = pd.merge(left = df_emails, right = df_info, how= 'left', left_on = 'cons_id', right_on = 'cons_id')

    # Create total data_frame for q1
    df_email_info_subs = pd.merge(
        left = df_email_info, right = df_subs, 
        how = 'left', 
        left_on = 'cons_email_id', right_on = 'cons_email_id')
        
    return df_email_info_subs


