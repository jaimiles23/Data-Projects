"""
Script to remove duplicates from dateaframes.

Appropriate duplicates were identified in jupyternb EDA
"""

##########
# Imports
##########

from typing import List, Union

import pandas as pd
import pywrangle as pw


##########
# Remove duplicates
##########

def remove_df_duplicates(df, column: str, keep: Union[str, bool] = False) -> "dataframe":
    """Auxiliary method to remove rows with duplicates n specified column.
    
    Uses pywrangle to record difference in df."""
    old_df = pw.record_df_info(df)
    df.drop_duplicates(subset = column, keep = keep, inplace = True)
    pw.print_df_changes(df, old_df)
    return df

