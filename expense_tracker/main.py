import urllib3
import urllib3.exceptions
import fastapi
import typer
from expense_tracker.api.v1.records import router as records_router
import expense_tracker.config
import uvicorn
import starlette.responses

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = fastapi.FastAPI(title="ExpenseTrackerAPI")
app.include_router(records_router)

cli_app = typer.Typer(add_completion=False)

@app.get("/")
def redirect_to_docs() -> None:
    """"""
    return starlette.responses.RedirectResponse("/docs")

@cli_app.callback(invoke_without_command=True)
def run() -> None:
    """"""
    config = expense_tracker.config.get_config()
    uvicorn.run(
        "expense_tracker.main:app",
        host=config.ip,
        port=config.port,
    )

def main():
    cli_app()

if __name__ == "__main__":
    main()

