import re

def remove_repeat_chars(string):
    chars = list(string)
    char_counts = {}
    for i, char in enumerate(string):
        if i in range(62, 96):
            char_counts[char] = char_counts.get(char, 0) + 1
    for char, count in char_counts.items():
        if count > 1:
            chars = [c for c in chars if c != char]
    return ''.join(chars)