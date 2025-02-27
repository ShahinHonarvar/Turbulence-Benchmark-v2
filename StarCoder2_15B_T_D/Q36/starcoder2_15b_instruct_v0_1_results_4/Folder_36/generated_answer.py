def filter_chars(text):
    """
    Filters characters from a string based on their index and value.
    """
    filtered_chars = []
    for i, char in enumerate(text):
        if i < 283 or i >= 484 or char <= 'l' or (char >= 't'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)