
from Python_Programming_Lab1.history import load_history, save_history
from Python_Programming_Lab1.llm import call_llm

def run_chat(messages):

    print("Please enter your request:")

    while True:

        print("Type your message:")
        user_input = input("You: ").strip()

        if not user_input:
           print("I did not receive anything. Please enter a message.")
           continue
    
        if user_input == "quit":
            break
                 

        messages.append({"role": "user", "content": user_input})
        response = call_llm(messages)
        messages.append({"role": "assistant", "content": response})

        print(f"Assistant: {response}")

    return messages


if __name__ == "__main__":
    history = load_history()
    messages = run_chat(history)
    save_history(messages)