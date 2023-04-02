import os
import tkinter as tk
import openai
from dotenv import load_dotenv

# Configure the OpenAI API key
load_dotenv()
str_openai_org = os.getenv("OPENAI_API_ORG")
str_openai_key = os.getenv("OPENAI_API_KEY")
openai.api_key = os.environ["OPENAI_API_KEY"]

# Function to generate response using OpenAI API
def generate_response(messages):
    completions = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.8,
    )

    message = completions.choices[0].message['content'].strip()
    return message

# Function to handle user input
def handle_input(event):
    user_message = user_input.get()
    user_input.delete(0, tk.END)
    
    if user_message.strip() == "/clear":
        chat_history.delete("1.0", tk.END)
        conversation_history.clear()
    else:
        chat_history.insert(tk.END, f"You: {user_message}\n")
        conversation_history.append({"role": "system", "content": f"You: {user_message}"})
        
        response = generate_response(conversation_history)
        chat_history.insert(tk.END, f"AI: {response}\n")
        conversation_history.append({"role": "assistant", "content": f"AI: {response}"})

# Create the main window
root = tk.Tk()
root.title("AI Chat Room")

# Create a text widget to display chat history
chat_history = tk.Text(root, wrap=tk.WORD, padx=5, pady=5)
chat_history.pack(expand=True, fill=tk.BOTH)

# Create an entry widget to get user input
user_input = tk.Entry(root)
user_input.pack(fill=tk.X, padx=5, pady=5)
user_input.bind("<Return>", handle_input)

# Initialize conversation_history
conversation_history = [{"role": "system", "content": "Chat with the AI"}]

root.mainloop()
