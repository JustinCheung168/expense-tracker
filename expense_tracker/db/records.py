"""expense-tracker db utilities."""
import pandas as pd
import os

import expense_tracker.config

class DBAccessError(Exception):
    """Error thrown when an attempt to access the database fails."""

# def get_records(year: str, source: str) -> pd.DataFrame:
#     """"""
#     try:
#         config = expense_tracker.config.get_config()
#         source_path = os.path.join(config.db_path,'records',year,source)
#         return pd.read_csv(source_path)
#     except:
#         raise DBAccessError("Failed to retrieve records from database")

