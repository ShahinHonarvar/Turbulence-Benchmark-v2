def remove_repeat_chars(string: str) -> str:
    """
    Removes repeated characters between indices 40 and 200 from a given string.
    """
    chars_to_remove = set()
    for i, char in enumerate(string[40:200]):
        if string[40:i].count(char) > 0:
            chars_to_remove.add(char)
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string