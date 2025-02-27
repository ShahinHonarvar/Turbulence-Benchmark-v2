def remove_repeat_chars(text):
    """
    Remove repeated characters from a string.
    """
    char_counts = {}
    for char in text[1:4]:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char, count in char_counts.items():
        if count > 1:
            text = text.replace(char, '')
    return text