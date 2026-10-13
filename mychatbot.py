import ollama

print("Welcome to My AI Chatbot!")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "user", "content": question}
        ]
    )

    print("AI:", response["message"]["content"]) 