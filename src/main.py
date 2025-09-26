Given the nature of your task, it seems to be about development work for a chatbot (Lyza) with a specific set of question types and categories for more accurate answers. However, without knowing the current state of "Lyza" or the specific categories and question types you want to enhance it with, it's hard to provide an exact code. 

Anyway, I'll provide a simplified code structure that may assist you. Assuming we are using a rule-based chatbot:

```python
class Lyza:
    def __init__(self):
        self.supported_categories = ['category1', 'category2']
        self.supported_question_types = ['type1', 'type2']

    def handle_question(self, category, question_type, question):
        if category not in self.supported_categories:
            return "I'm sorry, I don't support this category."
        
        if question_type not in self.supported_question_types:
            return "I'm sorry, I don't support this type of question."
        
        return self.generate_answer(category, question_type, question)
    
    def generate_answer(self, category, question_type, question):
        # Logic to generate answer based on category and question type
        return "Generated answer."

lyza = Lyza()

# Example usage:
response = lyza.handle_question('category1', 'type1', 'What is the weather like?')
print(response)
```

In this code:

1. An instance of Lyza is created with supported question categories and types. 
2. The method `handle_question` checks if Lyza supports the asked question's category and type. If not, it returns a message indicating the non-support. 
3. If Lyza can handle the asked question, it generates an answer with the `generate_answer` method where you should place the logic of answer generation.

Please adapt this according to your current chatbot's setup and requirements! The real implementation would be more complicated and might involve Natural Language Processing (NLP) libraries such as NLTK or frameworks like Rasa or Dialogflow from Google.