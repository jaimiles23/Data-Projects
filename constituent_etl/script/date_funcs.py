"""
Used to clean datetime of dfs
"""

##########
# Imports
##########

import re


##########
# Get Datetime
##########

## Auxiliary function to get datetime from day, datetime information stored in
def get_datetime(day_datetime: str) -> 'datetime':
    """Returns datetime object from str datetime.
    
    >>> get_datetime('sat, 2017-09-30 08:26:54') 
    2017-09-30 08:26:54
    """
    int_index = re.search(r'\d', day_datetime).start()
    datetime_list = list(day_datetime)[int_index:]
    return ''.join(datetime_list)
