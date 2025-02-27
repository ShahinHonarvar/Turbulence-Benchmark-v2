from collections import Counter

def remove_repeat_chars(text):
    counter = Counter(text)
    for char, count in counter.items():
        if count > 1 and 0 < text.index(char) < 6:
            text = text.replace(char, '')
    return text