from transformers import MarianMTModel, MarianTokenizer

MODEL_MAP = {
    "en": "Helsinki-NLP/opus-mt-id-en",
    "id": "Helsinki-NLP/opus-mt-en-id"
}

tokenizers = {}
models = {}

def translate_text(text: str, target_lang: str) -> str:
    if target_lang not in MODEL_MAP:
        return text

    if target_lang not in models:
        tokenizers[target_lang] = MarianTokenizer.from_pretrained(MODEL_MAP[target_lang])
        models[target_lang] = MarianMTModel.from_pretrained(MODEL_MAP[target_lang])

    tokenizer = tokenizers[target_lang]
    model = models[target_lang]

    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    translated = model.generate(**inputs)
    return tokenizer.decode(translated[0], skip_special_tokens=True)
