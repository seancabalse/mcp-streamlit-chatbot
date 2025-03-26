from fastapi import APIRouter
import PyPDF2

router = APIRouter()

@router.post("/summarize_pdf")
def summarize_pdf(payload: dict):
    path = payload.get("path")
    try:
        with open(path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            text = " ".join(page.extract_text() for page in reader.pages if page.extract_text())
            summary = text[:500] + "..." if len(text) > 500 else text
        return {"result": summary}
    except Exception as e:
        return {"result": f"Error reading PDF: {str(e)}"}
