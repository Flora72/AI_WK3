# Task 3: NER and Sentiment Analysis with spaCy
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Sample review
text = "I love my new Samsung Galaxy phone. It's way better than my old Nokia."

# Apply NLP pipeline
doc = nlp(text)

# Named Entity Recognition
print("Named Entities:")
for ent in doc.ents:
    print(ent.text, ent.label_)

# Rule-based sentiment analysis
positive_words = ["love", "great", "excellent", "amazing", "better"]
negative_words = ["bad", "worst", "poor", "hate"]

sentiment = "Positive" if any(word in text.lower() for word in positive_words) else "Negative"
print("Sentiment:", sentiment)
 