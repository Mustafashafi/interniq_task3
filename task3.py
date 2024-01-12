import nltk
from nltk.chat.util import Chat, reflections

# nltk.download('punkt')  # Uncomment and run this line if you haven't downloaded NLTK data

# Define patterns for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'How can I help you?']),
    (r'bye|goodbye', ['Goodbye!', 'See you!', 'Have a great day!']),
    (r'how are you', ["I'm a computer program, so I don't have feelings, but thanks for asking!"]),
    (r'what is your name', ["I'm a chatbot. You can call me ChatGPT."]),
    (r'my name is (.*)', ["Hello, {0}! How can I assist you today?"]),
    (r'(.*) help (.*)', ['Sure, I can help. What do you need assistance with?']),
    (r'(.*) your favorite (.*)', ["I'm just a program, so I don't have favorites."]),
    # Add more patterns as needed
]

# Create a chatbot using the defined patterns
chatbot = Chat(patterns, reflections)

def run_chatbot():
    print("Welcome! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()
        if user_input == 'bye':
            print("Goodbye!")
            break

        response = chatbot.respond(user_input)
        print("ChatGPT:", response)

if __name__ == "__main__":
    run_chatbot()
