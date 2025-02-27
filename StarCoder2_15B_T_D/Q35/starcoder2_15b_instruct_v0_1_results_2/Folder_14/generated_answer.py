def remove_repeat_chars(string):
    """
    This function removes repeated characters in a given string between indices 2 and 5,
    while preserving the order of all characters in the string.
    """
    char_count = {}
    for i, char in enumerate(string):
        if i >= 2 and i < 5:
            char_count[char] = char_count.get(char, 0) + 1
    for i, char in enumerate(string):
        if char_count.get(char, 0) > 1:
            string = string.replace(char, '')
    return string