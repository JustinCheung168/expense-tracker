"""API routes for accessing and visualizing financial records."""

import fastapi
import expense_tracker.api.v1.records_models as records_models

router = fastapi.APIRouter(tags=["records"], prefix="/expense_tracker/v1/records")

@router.get(
    "",
    response_model=list[records_models.Record],
    status_code=fastapi.status.HTTP_200_OK,
)
def get_records(
    year: str,
    source: str,
) -> list[records_models.Record]:
    """Returns a list of records."""
    return []

@router.get(
    "/echo",
    response_model=str,
    status_code=fastapi.status.HTTP_200_OK,
)
def echo(
    echo_str: str
) -> str:
    """"""
    return f"You said: {echo_str}"


