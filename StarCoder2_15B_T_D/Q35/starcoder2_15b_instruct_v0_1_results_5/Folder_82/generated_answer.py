from collections import Counter

def remove_repeat_chars(text: str) -> str:
    """
    Removes repeated characters in a given string between indices 30 and 200.
    """
    counter = Counter(text)
    result = []
    index = 0
    for char in text:
        if counter[char] == 1 or index < 30 or index >= 200:
            result.append(char)
        index += 1
    return ''.join(result)