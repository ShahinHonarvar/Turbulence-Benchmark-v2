def filter_chars(text: str) -> str:
    """
    Filters characters between indices 54 and 92 (exclusive) in a given text.
    """
    filtered_text = ''
    for i, char in enumerate(text):
        if i < 54 or i >= 92:
            filtered_text += char
        elif not (ord(char) > ord('J') and ord(char) < ord('X')):
            filtered_text += char
    return filtered_text