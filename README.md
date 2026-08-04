# AI Engineering Internship

This repository contains solutions for AI Engineering Internship tasks using pre-trained AI models.

## Task 1: Introduction Script

A simple Python script (`intro.py`) that prints a short introduction.

Run:

 ## bash
python intro.py

## Task 2: Sentiment Analysis

A sentiment analysis script using the Hugging Face Transformers library.

### Technologies
- Python
- Hugging Face Transformers
- PyTorch

Run:

```bash
python sentiment.py
```

---

## Task 3: OCR (Optical Character Recognition)

This project uses **EasyOCR**, a pre-trained deep learning model, to extract text from images.

### Technologies
- Python
- EasyOCR
- OpenCV
- Pillow

### Installation

```bash
pip install easyocr opencv-python pillow
```

### Usage

1. Place an image containing printed text in the project folder.
2. Rename the image to `sample.png`.
3. Run:

```bash
python ocr.py
```
## Task 5 – Spam Classifier

This project includes a simple machine learning spam classifier built with **scikit-learn**.

### Algorithm
- CountVectorizer
- Multinomial Naive Bayes

### Installation

## bash
pip install scikit-learn

### Run

## bash
python spam_classifier.py

## Task 6 – Improved Spam Classifier

The spam classifier was enhanced to improve prediction accuracy.

### Improvements
- Converted all text to lowercase.
- Removed punctuation using regular expressions.
- Replaced CountVectorizer with TF-IDF Vectorizer.
- Removed common English stop words.
- Expanded the training dataset with additional spam and non-spam examples.

# CLI Article Summarizer

## Description

This project is a command-line application that uses the OpenRouter LLM API to summarize articles.

## Prompt Design

The prompt instructs the model to:

- Act as a professional summarizer.
- Produce 3–5 bullet points.
- Focus on the most important information.
- Keep the summary concise and easy to understand.

## Installation

```bash
pip install requests
```

## Run

```bash
python summarizer_cli.py
```

## Task 8 – Streamlit Web Interface

This project includes a simple Streamlit web interface for the AI article summarizer.

### Installation

```bash
pip install streamlit requests
```

### Set API Key (PowerShell)

### Run

```bash
python -m streamlit run app.py
```

The application will open at:

```
http://localhost:8501
```