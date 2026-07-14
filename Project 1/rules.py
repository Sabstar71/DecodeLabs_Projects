from datetime import datetime

from data.intents import INTENTS, DEFAULT_RESPONSE, get_random_response


def normalize_text(text: str) -> str:
    return text.strip().lower()


def get_date() -> str:
    return datetime.now().strftime("%d %B %Y")


def get_time() -> str:
    return datetime.now().strftime("%I:%M %p")


def find_intent(user_input: str) -> str | None:
    user_input = normalize_text(user_input)

    for intent, data in INTENTS.items():
        if user_input in data["patterns"]:
            return intent

    return None


def get_rule_response(user_input: str) -> str:
    user_input = normalize_text(user_input)

    if user_input == "date":
        return f"Today's date is {get_date()}."

    if user_input == "time":
        return f"The current time is {get_time()}."

    intent = find_intent(user_input)

    if intent:
        return get_random_response(intent)

    return DEFAULT_RESPONSE