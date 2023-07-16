import requests
from bs4 import BeautifulSoup
import textwrap
import socket
import textwrap
import os


def display_text_in_box(text, width=40):
    def print_box_line(line):
        print(f"┃ {line}{' ' * (width - len(line))} ┃")

    wrapped_text = textwrap.fill(text, width=width)
    lines = wrapped_text.split('\n')
    max_line_length = max(len(line) for line in lines)

    box_top_bottom = "━" * (width + 2)

    print(f"┏{box_top_bottom}┓")
    for line in lines:
        print_box_line(line)
    print(f"┗{box_top_bottom}┛")


# Check if connected to the internet and run code accordingly


def is_connected_to_internet():
    try:
        # Attempt to connect to Google's DNS server (8.8.8.8) on port 53
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return True
    except OSError:
        pass
    return False


def randomVerse(display_text_in_box):
    # Make a request to the dailyverses.net website
    response = requests.get('https://dailyverses.net/random-bible-verse/kjv')

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the Bible verse element
    verse_element = soup.find(class_='v1')

    # Find the Bible book element
    book_element = soup.find(class_='vc')

    # Extract the verse text
    verse_text = verse_element.text.strip()

    # Extract the book text
    book_pick = book_element.text.strip()

    # Color the book text
    book = book_pick

    # blank text

    # text wrap
    verse = verse_text + \
        '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n' + book

    # Print the verse
    display_text_in_box(verse, width=30)


if is_connected_to_internet():
    randomVerse(display_text_in_box)
else:
    pass

