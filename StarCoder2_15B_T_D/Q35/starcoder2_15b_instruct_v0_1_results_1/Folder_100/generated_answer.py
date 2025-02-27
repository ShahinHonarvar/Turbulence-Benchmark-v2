from collections import Counter

def remove_repeat_chars(text: str) -> str:
    counter = Counter(text)
    for char, count in counter.items():
        if count > 1 and 44 < text.index(char) < 78:
            text = text.replace(char, '')
    return text