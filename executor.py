import subprocess
import platform


def execute_command(command):
    command = command.lower().strip()

    if "calculator" in command:
        if platform.system() == "Windows":
            subprocess.Popen("calc.exe")
            return "Opening calculator."

    elif "notepad" in command:
        if platform.system() == "Windows":
            subprocess.Popen("notepad.exe")
            return "Opening Notepad."

    elif "exit" in command or "quit" in command:
        return "EXIT"

    return "No executable action found."
