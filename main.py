import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_function import available_functions, call_function
from prompts import system_prompt


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

    final_text = None

    for i in range(20):
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=messages,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt, tools=[available_functions]
            ),
        )

        if response.usage_metadata is None:
            raise RuntimeError("failed api request")

        function_calls = response.function_calls or []

        if i == 0 and len(function_calls) == 0:
            raise RuntimeError("no function call")

        if response.text:
            final_text = response.text

        if len(function_calls) == 0:
            break

        func_res_parts = []

        for function_call in function_calls:
            function_call_result = call_function(function_call, verbose=args.verbose)

            if not function_call_result.parts:
                raise Exception("no parts return")

            part = function_call_result.parts[0]

            if part.function_response is None:
                raise Exception("no function response return")

            if part.function_response.response is None:
                raise Exception("no function response.response return")

            func_res_parts.append(part)

            if args.verbose:
                print(f"-> {part.function_response.response}")

        messages.append(types.Content(role="user", parts=func_res_parts))

    print("Final response:")
    if final_text is not None:
        print(final_text)

    if args.verbose and "response" in locals():
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
