import random

class SimpleChatbot:
    def __init__(self):
        self.responses = {
            "hello": ["Hi there!", "Hello!", "Greetings!", "How can I help you today?"],
            "how are you": ["I'm just a computer program, but thanks for asking!", "Doing well, how about you?", "I'm here to assist you!"],
            "what is your name": ["I'm a simple chatbot created to chat with you!", "You can call me Chatbot!", "I'm just a bot without a name."],
            "bye": ["Goodbye!", "See you later!", "Take care!"],
            "default": ["I'm not sure how to respond to that.", "Can you tell me more?", "Let's talk about something else!"]
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        for key in self.responses.keys():
            if key in user_input:
                return random.choice(self.responses[key])
        return random.choice(self.responses["default"])

def main():
    print("Welcome to the Simple Chatbot! Type 'bye' to exit.")
    chatbot = SimpleChatbot()

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()