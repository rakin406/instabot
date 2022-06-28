#!/usr/bin/env python3.7
"""
This is an Artificial Intelligence chatbot which talks with people on Instagram.
I call it "Rakin".
Usage: ./rakin.py <instagram>
"""

import sys
from instabot import Instabot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

ARGS = len(sys.argv) - 1
if ARGS == 0:
    print(
        "This is an Artificial Intelligence chatbot which talks with people on Instagram."
    )
    print("Usage: ./rakin.py <instagram>")
    sys.exit(1)

prev_msg = prev_bot_msg = "Hi, I am Rakin's chatbot."

bot = Instabot()
bot.find_person(' '.join(sys.argv[1:]))
print("Opened chat.")
bot.text_person(prev_bot_msg)

chatbot = ChatBot("Rakin")
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

while True:
    message = bot.get_message()
    bot_message = str(chatbot.get_response(message))

    # Message must not be the same as last message and it should not be from
    # the chatbot.
    if message != prev_msg and message != prev_bot_msg:
        bot.text_person(bot_message)
        prev_msg = message
        prev_bot_msg = bot_message
