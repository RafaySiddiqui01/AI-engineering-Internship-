import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data
messages = [
    "Congratulations! You won a free iPhone",
    "Claim your prize now",
    "Win cash today",
    "Limited time offer",
    "Free entry in a contest",
    "Click here to claim reward",
    "Hi, how are you?",
    "Let's meet tomorrow",
    "Can you send me the notes?",
    "See you at class",
    "Are we still meeting today?",
    "Please call me when you're free"
]

labels = [
    "Spam",
    "Spam",
    "Spam",
    "Spam",
    "Spam",
    "Spam",
    "Not Spam",
    "Not Spam",
    "Not Spam",
    "Not Spam",
    "Not Spam",
    "Not Spam"
]

# Text preprocessing
def preprocess(text):
    text = text.lower()                    
    text = re.sub(r'[^a-z0-9\s]', '', text) 
    return text

processed_messages = [preprocess(msg) for msg in messages]

# Better feature extraction using TF-IDF
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(processed_messages)

model = MultinomialNB()
model.fit(X, labels)


user_input = input("Enter a message: ")
processed_input = preprocess(user_input)
prediction = model.predict(vectorizer.transform([processed_input]))

print("\nPrediction:", prediction[0])