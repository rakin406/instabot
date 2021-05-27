#!/usr/bin/env python3
"""
Usage: ./cli.py <instagram>
"""

import sys
from instabot import Instabot

ARGS = len(sys.argv) - 1
if ARGS == 0:
    print("Usage: ./cli.py <instagram>")
    sys.exit(1)

bot = Instabot()
bot.find_person(sys.argv[1])
bot.text_person(
    'Hello {}. This program is written by Rakin. You can start using me by saying "start".'.format(
        sys.argv[1]
    )
)

while True:
    if bot.get_message() == "start":
        bot.text_person("Hello {} :)".format(sys.argv[1]))
