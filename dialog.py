def get_response(command):
    command = command.lower().strip()

    if "hello" in command or "hi" in command:
        return "Hello! How can I help you?"

    elif "status" in command:
        return "System is authenticated and ready."

    elif "time" in command:
        return "The system is currently running."

    elif "help" in command:
        return "Available commands: open calculator, open notepad, status, exit."

    elif "exit" in command or "quit" in command:
        return "Goodbye!"

    else:
        return "I don't understand that command."
