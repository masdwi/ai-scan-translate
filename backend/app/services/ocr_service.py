import easyocr
import numpy as np
from PIL import Image
import io

reader = easyocr.Reader(['id', 'en'])

def extract_text(image_bytes: bytes) -> str:
    image = Image.open(io.BytesIO(image_bytes))
    image_np = np.array(image)
    results = reader.readtext(image_np)
    text = " ".join([res[1] for res in results])
    return text
