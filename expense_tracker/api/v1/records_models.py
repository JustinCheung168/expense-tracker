
import pydantic

class Record(pydantic.BaseModel):
    """Model class representing a financial record.
    
    Attributes:
        account: The account that provides the information for this record.
        date:
        description: The description that the record comes with.
        amount: The dollar and cents amount of money the record describes.
    """

    account: str

    date: str
    description: str
    amount: float

