import re

def filter_chars(text):
    filtered_text = ''
    for char in text:
        if not (48 < ord(char) < 75 and char > '6' and (char < '_')):
            filtered_text += char
    return filtered_text