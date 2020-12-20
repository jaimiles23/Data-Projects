"""
Script to only keep relevant column data. This is used to increase performance.
"""

##########
# Imports
##########

from typing import List

import pandas as pd


##########
# Keep df_cols
##########

def keep_df_cols(df: object, columns: list) -> object:
    """AUxiliary function to returns pandas dataframe with only specified columns.
    
    Uses pywrangle to document df changes."""
    df = df[columns]
    return df
