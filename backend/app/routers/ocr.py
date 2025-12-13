from fastapi import APIRouter, UploadFile, File
from app.services.ocr_service import extract_text
from app.services.translate_service import translate_text

router = APIRouter(prefix="/ocr", tags=["OCR"])

@router.post("/scan-translate")
async def scan_and_translate(
    file: UploadFile = File(...),
    target_lang: str = "en"
):
    text = extract_text(await file.read())
    translated = translate_text(text, target_lang)
    return {
        "original_text": text,
        "translated_text": translated
    }