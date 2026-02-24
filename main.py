import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    if api_key is None:
        raise RuntimeError("no api key provided")

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    object = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=messages,
    )

    if object.usage_metadata is None:
        raise RuntimeError("failed api request")

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {object.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {object.usage_metadata.candidates_token_count}")

    print(object.text)


if __name__ == "__main__":
    main()
