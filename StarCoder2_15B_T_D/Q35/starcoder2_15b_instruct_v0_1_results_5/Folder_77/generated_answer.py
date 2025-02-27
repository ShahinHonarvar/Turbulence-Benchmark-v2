def remove_repeat_chars(text):
    """
    Removes repeated characters from a string between indices 355 and 988.
    """
    char_counts = {}
    for char in text[355:988]:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char, count in char_counts.items():
        if count > 1:
            text = text.replace(char, '')
    return text