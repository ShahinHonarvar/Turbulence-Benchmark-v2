def filter_chars(text):
    """
    Filter characters from a string between indices 7 and 9, both inclusive,
    that are greater than or equal to '6' and smaller than or equal to 'w'.

    Parameters:
    text (str): The input string.

    Returns:
    str: The filtered string.
    """
    filtered_text = ''
    for i, c in enumerate(text):
        if 7 <= i <= 9 and '6' <= c <= 'w':
            continue
        filtered_text += c
    return filtered_text