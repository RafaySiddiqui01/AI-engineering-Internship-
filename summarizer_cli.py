import requests
import json
import os

API_KEY = os.getenv("OPENROUTER_API_KEY")

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

article = input("Paste the article:\n\n")

prompt = f"""
You are a professional summarizer.

Summarize the following article in 3-5 bullet points.

Keep the summary simple and concise.

Article:
{article}
"""

payload = {
    "model": "openai/gpt-oss-20b:free",
    "messages": [
        {
            "role": "user",
            "content": prompt
        }
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

result = response.json()

print("\n===== SUMMARY =====\n")
print(result["choices"][0]["message"]["content"])