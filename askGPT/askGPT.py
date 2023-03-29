# file: askGPT.py

from response import get_response

if __name__ == "__main__":
    # Print a welcome message.
    print("Ask GPT-3\n")

    # Start a loop to prompt the user for input and generate responses.
    while True:
        # Get user input.
        user_input = input("You: ")

        # Generate a response based on the user input.
        response = get_response(user_input)

        # Print the response.
        print("\nGPT: " + response)

        # Prompt the user to continue or exit.
        print("\n")
        print("Continue? (y/n): ", end="")
        if input() == "n":
            break
