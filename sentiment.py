from transformers import pipeline

classifier = pipeline("sentiment-analysis")

text = input("Enter a sentence: ")

result = classifier(text)

print("\nResult:")
print(f"Label: {result[0]['label']}")
print(f"Confidence: {result[0]['score']:.2f}")