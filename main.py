import os
from dotenv import load_dotenv
from google import genai
import sys

def main():
    load_dotenv()

    args = sys.argv[1:] # Get command line arguments

    if not args: # Check if there is any argument provided
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    user_prompt = " ".join(args)  # Join arguments to form the prompt

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=user_prompt)
    text = response.text
    print(text)
    usage = response.usage_metadata
    print(f"Prompt tokens: {usage.prompt_token_count}")
    print(f"Response tokens: {usage.candidates_token_count}")


if __name__ == "__main__":
    main()
