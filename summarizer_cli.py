import os
import json
import requests

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    print("Error: OPENROUTER_API_KEY is not set.")
    exit()

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "http://localhost",
    "X-Title": "AI Engineering Internship"
}

article = input("Paste the article:\n\n")

prompt = f"""
You are a professional summarizer.

Summarize the following article in 3–5 bullet points.

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

response = requests.post(url, headers=headers, json=payload)

print("Status Code:", response.status_code)

try:
    result = response.json()
except Exception:
    print("Response was not valid JSON.")
    print(response.text)
    exit()

if response.status_code != 200:
    print("API Error:")
    print(result)
    exit()

print("\n===== SUMMARY =====\n")
print(result["choices"][0]["message"]["content"])