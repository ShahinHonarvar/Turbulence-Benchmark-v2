from collections import Counter

def remove_repeat_chars(text: str) -> str:
    """
    Function to remove repetitive characters from a string.
    """
    counter = Counter(text)
    for char, count in counter.items():
        if count > 1:
            text = text.replace(char, '')
    return text