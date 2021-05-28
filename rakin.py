#!/usr/bin/env python3
"""
Rakin is the name of the author of this program.
Usage: ./rakin.py <instagram>
"""

import sys
import random
from instabot import Instabot

ARGS = len(sys.argv) - 1
if ARGS == 0:
    print("Usage: ./rakin.py <instagram>")
    sys.exit(1)

bot = Instabot()
bot.find_person(sys.argv[1])
bot.text_person(
    "Yo. I am Rakin's chatbot. I'll try to act like him as much as possible.\
            Commands: \"yo\"."
)

GREETINGS = ["sup", "yo"]
ANSWERS = ["Ask that to Rakin, not me", "do i look smart to u? lol"]
command_triggered = 0

while True:
    message = bot.get_message()
    if str(message).endswith("?"):
        bot.text_person(random.choice(ANSWERS))
    elif message == "yo":
        if command_triggered < 5:
            bot.text_person(random.choice(GREETINGS))
        elif command_triggered == 5:
            bot.text_person(random.choice(["bruh", "lol"]))
        else:
            bot.text_person("SUP SUP SUP SUP SUP SUP SUP SUP SUP")
        command_triggered += 1
