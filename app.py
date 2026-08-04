import os
import requests
import streamlit as st

API_KEY = os.getenv("OPENROUTER_API_KEY")

st.set_page_config(page_title="AI Summarizer", page_icon="📝")

st.title("📝 AI Article Summarizer")
st.write("Paste an article below and click **Summarize**.")

article = st.text_area("Article", height=250)

if st.button("Summarize"):

    if not API_KEY:
        st.error("OPENROUTER_API_KEY is not set.")
        st.stop()

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "AI Engineering Internship"
    }

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

    with st.spinner("Generating summary..."):

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload
        )

        if response.status_code == 200:
            result = response.json()
            st.subheader("Summary")
            st.write(result["choices"][0]["message"]["content"])
        else:
            st.error(response.json())