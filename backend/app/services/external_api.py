import requests
import httpx
import os
from typing import Dict, Optional
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

class ExternalAPIService:
    
    @staticmethod
    def get_country_currency(country_name: str) -> Optional[str]:
        """Fetch currency for a country from REST Countries API"""
        try:
            response = requests.get(
                "https://restcountries.com/v3.1/all?fields=name,currencies",
                timeout=10
            )
            if response.status_code == 200:
                countries = response.json()
                for country in countries:
                    if country.get("name", {}).get("common", "").lower() == country_name.lower():
                        currencies = country.get("currencies", {})
                        if currencies:
                            return list(currencies.keys())[0]
            return "USD"  # Default fallback
        except Exception as e:
            print(f"Error fetching country currency: {e}")
            return "USD"
    
    @staticmethod
    def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
        """Convert currency using Exchange Rate API"""
        if from_currency == to_currency:
            return amount
        
        try:
            response = requests.get(
                f"https://api.exchangerate-api.com/v4/latest/{from_currency}",
                timeout=10
            )
            if response.status_code == 200:
                data = response.json()
                rate = data.get("rates", {}).get(to_currency, 1.0)
                return round(amount * rate, 2)
            return amount
        except Exception as e:
            print(f"Error converting currency: {e}")
            return amount
    
    @staticmethod
    async def extract_text_from_receipt(image_data: bytes) -> Dict:
        """Extract text from receipt using Hugging Face OCR"""
        try:
            # Using Microsoft's TrOCR model for receipt OCR
            API_URL = "https://api-inference.huggingface.co/models/microsoft/trocr-base-printed"
            headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
            
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(API_URL, headers=headers, content=image_data)
                
                if response.status_code == 200:
                    result = response.json()
                    # Extract text from response
                    if isinstance(result, list) and len(result) > 0:
                        extracted_text = result[0].get("generated_text", "")
                    else:
                        extracted_text = str(result)
                    
                    # Parse extracted text for amount, date, vendor
                    parsed_data = ExternalAPIService._parse_receipt_text(extracted_text)
                    return parsed_data
                else:
                    return {"text": "", "amount": None, "date": None, "vendor": None}
        except Exception as e:
            print(f"Error extracting text from receipt: {e}")
            return {"text": "", "amount": None, "date": None, "vendor": None}
    
    @staticmethod
    def _parse_receipt_text(text: str) -> Dict:
        """Parse receipt text to extract structured data"""
        import re
        from datetime import datetime
        
        # Simple parsing logic (can be enhanced)
        amount = None
        date = None
        vendor = None
        
        # Extract amount (look for currency symbols and numbers)
        amount_pattern = r'[\$€£¥₹]\s*(\d+\.?\d*)'
        amount_match = re.search(amount_pattern, text)
        if amount_match:
            amount = float(amount_match.group(1))
        
        # Extract date patterns
        date_patterns = [
            r'\d{2}/\d{2}/\d{4}',
            r'\d{2}-\d{2}-\d{4}',
            r'\d{4}-\d{2}-\d{2}'
        ]
        for pattern in date_patterns:
            date_match = re.search(pattern, text)
            if date_match:
                date = date_match.group(0)
                break
        
        # Extract vendor (first line usually)
        lines = text.split('\n')
        if lines:
            vendor = lines[0].strip()[:50]
        
        return {
            "text": text,
            "amount": amount,
            "date": date,
            "vendor": vendor
        }
    
    @staticmethod
    async def classify_expense_category(description: str) -> str:
        """Classify expense category using Hugging Face NLP"""
        try:
            # Using zero-shot classification
            API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"
            headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
            
            categories = [
                "travel", "meals", "accommodation", "office_supplies",
                "entertainment", "transportation", "utilities", "software",
                "training", "other"
            ]
            
            payload = {
                "inputs": description,
                "parameters": {
                    "candidate_labels": categories
                }
            }
            
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(API_URL, headers=headers, json=payload)
                
                if response.status_code == 200:
                    result = response.json()
                    if "labels" in result and len(result["labels"]) > 0:
                        return result["labels"][0]
                    return "other"
                else:
                    return "other"
        except Exception as e:
            print(f"Error classifying expense category: {e}")
            return "other"
