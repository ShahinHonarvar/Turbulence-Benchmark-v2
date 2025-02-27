def remove_repeat_chars(text):
    """
    Remove repeated characters from a string between indices 22 and 24.
    """
    char_counts = {}
    for i, char in enumerate(text):
        if i >= 22 and i < 24:
            char_counts[char] = char_counts.get(char, 0) + 1
    for char, count in char_counts.items():
        if count > 1:
            text = text.replace(char, '')
    return text