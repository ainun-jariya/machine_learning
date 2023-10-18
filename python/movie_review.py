# Import libraries
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Sample data (movie reviews and their labels)
reviews = [
    "This movie is great and wonderful!",
    "I enjoyed watching this film a lot.",
    "Not a good movie. Disappointed.",
    "Waste of time. Terrible acting.",
]
labels = ['positive', 'positive', 'negative', 'negative']

# Text vectorization (converting text to numerical features)
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(reviews)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# Train a text classifier
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# Make predictions
y_pred = classifier.predict(X_test)

# Evaluate the classifier
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Print results
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(report)
