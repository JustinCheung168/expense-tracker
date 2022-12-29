"""Configuration for expense-tracker."""

import pydantic

class ExpenseTrackerConfig(pydantic.BaseSettings):
    """"""
    ip: str = "127.0.0.1"
    port: int = 5001
    db_path: str = "db-private/"


_config: ExpenseTrackerConfig

def get_config() -> ExpenseTrackerConfig:
    """"""
    global _config
    _config = ExpenseTrackerConfig()
    return _config
