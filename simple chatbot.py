class SimpleChatbot:
    def __init__(self):
        self.responses = {
            "hello": "Hi there! How can I help you?",
            "how are you": "I'm just a chatbot, but thanks for asking!",
            "bye": "Goodbye! Have a great day.",
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        return self.responses.get(user_input, "I'm sorry, I don't understand that.")

# Example of using the chatbot
chatbot = SimpleChatbot()

while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break

    response = chatbot.get_response(user_input)
    print("Chatbot:", response)
