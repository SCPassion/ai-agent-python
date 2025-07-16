import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from functions.get_files_info import config
import sys


def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv  # Check if verbose flag is present
    if verbose:
        args = sys.argv[1:-1]  # Exclude the last argument which is --verbose
    else:
        args = sys.argv[1:] # Get command line arguments

    if not args: # Check if there is any argument provided
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    user_prompt = " ".join(args)  # Join arguments to form the prompt
    if verbose:
        print(f"User prompt: {user_prompt}")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    generate_content(client, messages, verbose)
    

def generate_content(client, messages, verbose):
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages, config=config)
    text = response.text
    function_calls = response.function_calls;
    usage = response.usage_metadata

    if verbose:
        print(f"Prompt tokens: {usage.prompt_token_count}")
        print(f"Response tokens: {usage.candidates_token_count}")

    print("Response:")
    if not function_calls:
        print(response.text)
        return text
    else:
        for function_call in function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")

if __name__ == "__main__":
    main()