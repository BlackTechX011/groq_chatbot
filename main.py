import os
import json
import sys
from groq import Groq

def clear():
    _ = os.system('cls' if os.name == 'nt' else 'clear')
def main():
    # Get API key from environment variable
    api_key = "Enter your groq cloud api key"

    # Load existing conversation data from file or create a new one
    if os.path.exists("data.json"):
        with open("data.json", "r") as file:
            data = json.load(file)
    else:
        data = {"messages": []}

    # Prompt user for input
    user_input = input("You: ")

    # Check for special commands
    if user_input.lower() == 'exit':
        sys.exit()
    elif user_input.lower() == '-newchat':
        clear()
        new_chat()
        main()
    elif user_input.lower() == '-help':
        clear()
        print("\nGroq API-based self-learning AI bot")
        print("Available Commands:")
        print("[ -help ]    Display help menu")
        print("[ -newchat ] Reset the chat and start a new conversation")
        print("[ exit ]     Exit the program")
        print("[ -restart ] Restart the script")
        print("This tool is under development")
        main()
    elif user_input.lower() == '-restart':
       clear()
       os.system('python main.py' if os.name == 'nt' else 'python3 main.py')
    else:
        # User's content
        user_content = {"role": "user", "content": user_input}
        data["messages"].append(user_content)

        # Initialize Groq client with API key
        client = Groq(api_key=api_key)

        # Get completion from Groq
        chat_completion = client.chat.completions.create(messages=data["messages"], model="mixtral-8x7b-32768")

        # Extract bot's response
        bot_response = chat_completion.choices[0].message.content

        # Bot's content
        bot_content = {"role": "assistant", "content": bot_response}
        data["messages"].append(bot_content)

        # Write modified conversation data back to file
        with open("data.json", "w") as file:
            json.dump(data, file, indent=2)

        # Print bot's response
        print("Bot:", bot_response)
        main()

def new_chat():
    content_to_keep = {
  "messages": [
    {
      "role": "system",
      "content": "you are a helpful assistant."
    }
  ]
}
    with open("data.json", "w") as file:
        json.dump(content_to_keep, file, indent=2)

if __name__ == "__main__":
    main()
