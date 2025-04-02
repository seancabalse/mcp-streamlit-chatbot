from fastapi import APIRouter
import PyPDF2
import os
import sys

router = APIRouter()


@router.post("/summarize_pdf")
def summarize_pdf(payload: dict):
    # Get the PDF path from environment variable or use a default
    pdf_path = os.environ.get("PDF_PATH")

    # Debug information
    print(f"Current directory: {os.getcwd()}")
    print(f"Script location: {os.path.dirname(os.path.abspath(__file__))}")
    print(f"PDF path: {pdf_path}")
    print(f"PDF exists: {os.path.exists(pdf_path)}")

    try:
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            text = " ".join(
                page.extract_text() for page in reader.pages if page.extract_text()
            )
            summary = text[:500] + "..." if len(text) > 500 else text
        return {"result": summary}
    except Exception as e:
        return {
            "result": f"Error reading PDF: {str(e)}\nDebug info:\nPDF path: {pdf_path}\nFile exists: {os.path.exists(pdf_path)}"
        }
