As an AI, I gather you may want me to enhance a program (Lyza) to be able to understand and categorize various types of questions better. In this prototype, let's assume Lyza is an AI chatbot which accepts a question from the user, identifies question type and category for a better response. 

```python
import spacy

# Load the SpaCy model
nlp = spacy.load('en_core_web_sm')

question_categories = {
    "what": "Entity",
    "where": "Location",
    "when": "Time",
    "who": "Person",
    "why": "Reason",
    "how": "Method",
}

question_types = {
    "what": "Open-ended",
    "where": "Closed-ended",
    "when": "Closed-ended",
    "who": "Closed-ended",
    "why": "Open-ended",
    "how": "Open-ended",
}

def categorize_question(question):
    doc = nlp(question.lower())
    for token in doc:
        if token.text in question_categories:
            return question_categories[token.text], question_types[token.text]
    return "Unknown", "Unknown"

# Test the function
question = "Where is the Eiffel Tower?"
category, qtype = categorize_question(question)
print(f"Question: {question}")
print(f"Category: {category}")
print(f"Type: {qtype}")
```

In this code, I have considered six basic types of questions. 'SpaCy' is used to parse the question and detect the type of the question. Please replace `'en_core_web_sm'` with the model of your choice based on your own requirement.

Please note, creating a fully functioning program Lyza considering all edge cases would require a more advanced Natural Language Processing and certainly more details of your requirement.