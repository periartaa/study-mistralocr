import os
from mistralai import Mistral
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve the API key from environment variables
MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY')
client = Mistral(api_key=MISTRAL_API_KEY)

ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document={
        "type": "document_url",
        "document_url": "https://arxiv.org/pdf/2201.04234"
    },
    include_image_base64=True
)