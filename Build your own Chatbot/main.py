import tkinter as tk

# Create a function to handle user input and bot responses
def send_message():
    user_input = entry.get()
    entry.delete(0, tk.END)  # Clear the input field

    # Display user message
    display_message(f'You: {user_input}', 'user')

    user_input = user_input.lower()

    # Bot responses
    if user_input == "hello":
        display_message("Bot: Hi there, how can I help?")
    elif user_input in ["hi", "hii", "hiiii"]:
        display_message("Bot: Hi there, what can I do for you?")
    elif user_input == "how are you":
        display_message("Bot: Fine! And you?")
    elif user_input in ["fine", "i am good", "i am doing good"]:
        display_message("Bot: Great! How can I help you?")
    elif user_input in ["thanks", "thank you", "now its my time"]:
        display_message("Bot: My pleasure!")
    elif user_input in ["what do you sell", "what kinds of items are there", "have you something"]:
        display_message("Bot: We have coffee and tea.")
    elif user_input in ["tell me a joke", "tell me something funny", "crack a funny line"]:
        display_message('Bot: What did the buffalo say when his son left for college? Bison!')
    elif user_input in ["goodbye", "see you later", "see yaa"]:
        display_message('Bot: Have a nice day!')
    else:
        display_message('Bot: Sorry! I did not understand that.')

# Create a function to display messages in the chat
def display_message(message, sender='bot'):
    if sender == 'user':
        message_color = 'blue'
    else:
        message_color = 'green'

    chat_text.config(state=tk.NORMAL)  # Enable text widget for editing
    chat_text.insert(tk.END, message + '\n', message_color)  # Insert message with specified color
    chat_text.config(state=tk.DISABLED)  # Disable text widget for editing

# Create the main GUI window
root = tk.Tk()
root.title("Chatbot")

# Create a text widget for the chat history
chat_text = tk.Text(root, bg="#2C3E50", fg="white", font=("Helvetica", 14), width=50, height=20)
chat_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create an entry widget for user input
entry = tk.Entry(root, bg="white", fg="black", font=("Helvetica", 12), width=40)
entry.grid(row=1, column=0, padx=10, pady=10)

# Create a send button to submit user input
send_button = tk.Button(root, text="Send", font=("Helvetica", 12, "bold"), bg="#3498DB", fg="white", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Start the GUI main loop
root.mainloop()
