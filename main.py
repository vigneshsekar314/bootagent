from google.genai import Client, types
from dotenv import load_dotenv
from os import getenv
import sys


def main():

    cmd_arguments = sys.argv[1:]

    if cmd_arguments is None or len(cmd_arguments) == 0:
        sys.exit(1)
    load_dotenv()
    gemini_api_key = getenv("GEMINI_API_KEY")

    user_prompt = cmd_arguments[0]

    client = Client(api_key=gemini_api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]
    model_res = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
    print(model_res.text)
    assert model_res is not None and model_res.usage_metadata is not None, "model response usage metadata is None"
    if model_res is not None and model_res.usage_metadata is not None and "--verbose" in cmd_arguments:
            print(f"User prompt: {user_prompt}")
            print(f"Prompt tokens: {model_res.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {model_res.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
