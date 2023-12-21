# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 14:54:34 2023

@author: idalin
"""


import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and their corresponding responses related to Canada Post order tracking
pairs = [
    [
        r"Hello",
        ["Hello! Welcome to Canada Post order tracking support. How can I assist you?",]
    ],
    [
        r"My order number is (.*)",
        ["I will check your order number so I can track it for you.",]
    ],
    [
        r"Can you track my order with number (.*)",
        ["Absolutely, I'll help you track your order with number %1.",]
    ],
    [
        r"Where is my package?",
        ["Let me check the status of your order. Please provide the order number.",]
    ],
    [
        r"Where's my parcel?",
        ["To assist you, I need your order number to track the parcel.",]
    ],
    [
        r"exit",
        ["Thank you for reaching out to Canada Post order tracking support. Have a great day!",]
    ],
    [
        r"How are you?",
        ["I'm here to assist with Canada Post order tracking. How can I help you today?",]
    ],
    [
        r"What can you do?",
        ["I can help you track your Canada Post orders. Just provide me with your order number!",]
    ],
    [
        r".*help.*",
        ["Sure, I can assist you with Canada Post order tracking. Please provide the order number.",]
    ],
    [
        r".*order.*",
        ["Please provide the order number so I can track your Canada Post order for you.",]
    ],
    # Add more patterns and responses as needed
]

# Define reflections
reflections = {
    "I": "you",
    "I am": "you are",
    "my": "your",
    "I can": "you can",
    "I will": "you will",
    "I want": "you want",
    "I'm": "you're",
    # Add more reflections as needed
}

# Define a function to initiate the chat process
def chat():
    print("Hello! Welcome to Canada Post order tracking support.")
    print("I'm here to assist you with tracking your orders.")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

# Start the conversation
if __name__ == "__main__":
    chat()
