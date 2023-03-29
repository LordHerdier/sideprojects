import openai
import os
import sys

def get_response(prompt):
    """
    Generates a response using OpenAI's GPT-3 language model based on the given prompt.
    Requires an OpenAI API key to be set in the OPENAI_API_KEY environment variable.

    Args:
    - prompt (str): The prompt to generate a response for.

    Returns:
    - response (str): The generated response based on the prompt.
    """

    # Set the API key for OpenAI.
    try:
        openai.api_key = os.getenv("OPENAI_API_KEY")
    except:
        print("No API key found")
        sys.exit(1)

    # Use OpenAI's Completion API to generate a response.
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            temperature=0.5,
            max_tokens=100,
            n=1,
            stop=None,
            timeout=60,
        )

        # Extract the response text from the API's response.
        response = response.choices[0].text.strip()
        return response

    except Exception as e:
        # Raise any exceptions encountered during the API call.
        raise e