import random

INTENTS = {
    "greeting": {
        "patterns": [
            "hi",
            "hello",
            "hey",
            "good morning",
            "good evening",
            "good afternoon"
        ],
        "responses": [
            "Hello! How can I help you today?",
            "Hi! Nice to meet you.",
            "Hello! What can I do for you?"
        ]
    },

    "thanks": {
        "patterns": [
            "thanks",
            "thank you",
            "thankyou"
        ],
        "responses": [
            "You're welcome.",
            "Happy to help.",
            "Anytime."
        ]
    },

    "about": {
        "patterns": [
            "who are you",
            "what are you",
            "about yourself"
        ],
        "responses": [
            "I am a Rule-Based Chatbot built using Python."
        ]
    },

    "ai": {
        "patterns": [
            "what is ai",
            "define ai",
            "artificial intelligence"
        ],
        "responses": [
            "Artificial Intelligence is the simulation of human intelligence in machines."
        ]
    },

    "developer": {
        "patterns": [
            "developer",
            "who made you",
            "creator"
        ],
        "responses": [
            "I was developed by Sabeeh Waheed as part of the DecodeLabs AI Internship."
        ]
    },

    "help": {
        "patterns": [
            "help",
            "commands",
            "menu"
        ],
        "responses": [
            """Available commands:

• hello
• thanks
• who are you
• what is ai
• date
• time
• developer
• exit"""
        ]
    },

    "exit": {
        "patterns": [
            "bye",
            "exit",
            "quit",
            "goodbye"
        ],
        "responses": [
            "Goodbye. Have a great day!"
        ]
    }
}


DEFAULT_RESPONSE = (
    "Sorry, I couldn't understand that. "
    "Please try another question or type 'help'."
)


def get_random_response(intent):
    return random.choice(INTENTS[intent]["responses"])