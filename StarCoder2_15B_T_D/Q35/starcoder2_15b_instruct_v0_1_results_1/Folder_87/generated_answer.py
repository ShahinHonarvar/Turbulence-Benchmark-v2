def remove_repeat_chars(string: str) -> str:
    """
    Removes repeated characters in a given string between indices 20 and 43, both exclusive.
    """
    for char in set(string[20:43]):
        if string.count(char) > 1:
            string = string.replace(char, '')
    return string