responses = {
    "hello": "Hi! How can I help you?",
    "hi": "Hello! What would you like to know?",
    "ai": "AI stands for Artificial Intelligence. It enables machines to think and learn.",
    "machine learning": "Machine learning is a subset of AI that allows systems to learn from data.",
    "bye": "Goodbye! Have a great day!"
}

print("AI Chatbot 🤖 (type 'bye' to exit)\n")

while True:
    user = input("You: ").lower()

    if user in responses:
        print("Bot:", responses[user])
    else:
        print("Bot: I am still learning! Try asking something else.")
    
    if user == "bye":
        break