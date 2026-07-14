from openai import OpenAI

from config import OPENROUTER_API_KEY, MODEL


def get_ai_client():
    if not OPENROUTER_API_KEY:
        return None

    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENROUTER_API_KEY
    )


def get_ai_response(messages):
    client = get_ai_client()

    if client is None:
        return "OpenRouter API key not found."

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.7,
            max_tokens=500,
        )

        return response.choices[0].message.content

    except Exception:
        return "Unable to connect to the AI model. Please try again later."