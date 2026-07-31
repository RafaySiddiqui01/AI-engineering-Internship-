from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data
messages = [
    "Congratulations! You won a free iPhone",
    "Claim your prize now",
    "Win cash today",
    "Limited time offer",
    "Hi, how are you?",
    "Let's meet tomorrow",
    "Can you send me the notes?",
    "See you at class"
]

labels = [
    "Spam",
    "Spam",
    "Spam",
    "Spam",
    "Not Spam",
    "Not Spam",
    "Not Spam",
    "Not Spam"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)

model = MultinomialNB()
model.fit(X, labels)

text = input("Enter a message: ")

prediction = model.predict(vectorizer.transform([text]))

print("\nPrediction:", prediction[0])