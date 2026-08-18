from face_auth import authenticate_face
from dialog import get_response
from executor import execute_command


def main():

    print("=" * 50)
    print("       END-TO-END AI CAPSTONE")
    print("=" * 50)

    # Step 1: Authentication
    authenticated = authenticate_face()

    if not authenticated:
        print("Authentication failed.")
        return

    print("\nAuthentication successful!")

    # Step 2: Dialog + commands
    while True:

        command = input("\nEnter command: ")

        response = get_response(command)
        print("Assistant:", response)

        # Step 3: Execute command
        result = execute_command(command)

        if result != "No executable action found.":
            print("Executor:", result)

        if result == "EXIT":
            break


if __name__ == "__main__":
    main()
