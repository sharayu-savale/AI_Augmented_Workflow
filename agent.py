def chatbot():
    """
    A simple chatbot function that interacts with the user.
    """
    print("Hello! I am your friendly chatbot. How can I assist you today?")

    while True:
        user_input = input("You: ")
        text = user_input.lower()

        if text in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye! Have a great day!")
            break

        elif "hello" in text or "hi" in text:
            print("Chatbot: Hello! Nice to meet you.")

        elif "name" in text:
            print("Chatbot: I am a simple AI chatbot.")

        elif "artificial intelligence" in text or "what is ai" in text:
            print("Chatbot: Artificial Intelligence (AI) is a technology that enables computers to perform tasks that normally require human intelligence.")

        elif "machine learning" in text:
            print("Chatbot: Machine Learning is a branch of AI that allows computers to learn from data and improve their performance.")

        elif "python" in text:
            print("Chatbot: Python is a popular programming language used for AI, Machine Learning, data science, and automation.")

        else:
            print("Chatbot: Sorry, I don't understand.")


chatbot()