def filter_chars(text):
    """Filter characters in a string based on their position and value."""
    filtered_text = ''
    for i, c in enumerate(text):
        if 31 <= i < 50 and (not '/' < c < 'J'):
            filtered_text += c
    return filtered_text