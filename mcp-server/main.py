from fastapi import FastAPI
from tools.summarize_pdf import router as summarize_router

app = FastAPI()
app.include_router(summarize_router, prefix="/tools")
