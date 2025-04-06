import os
from dotenv import load_dotenv
from mistralai import Mistral

# Muat variabel dari .env
load_dotenv()

# Ambil API key
api_key = os.getenv("MISTRAL_API_KEY")
if not api_key:
    raise ValueError("API key tidak ditemukan. Pastikan MISTRAL_API_KEY ada di file .env.")

# Inisialisasi client Mistral
client = Mistral(api_key=api_key)

# Jalankan proses OCR
ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document={
        "type": "document_url",
        "document_url": "https://arxiv.org/pdf/2201.04234"
    },
    include_image_base64=True
)

# Cetak hasilnya
print(ocr_response)
