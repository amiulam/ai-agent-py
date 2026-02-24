import os

from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def main():
    print("Hello from ai-agent-py!")
    if api_key is None:
        raise RuntimeError("no api key provided")

    object = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
    )

    print(object.text)


if __name__ == "__main__":
    main()
