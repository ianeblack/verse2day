import requests
from bs4 import BeautifulSoup
import textwrap

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
book = book_element.text.strip()

# text wrap
verse = textwrap.fill(verse_text, width=30)


# Print the verse
print("")
print(verse)
print(book)
print("")


