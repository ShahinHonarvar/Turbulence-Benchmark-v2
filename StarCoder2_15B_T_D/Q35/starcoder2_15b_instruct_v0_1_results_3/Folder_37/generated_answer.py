def remove_repeat_chars(string):
    """
    Removes repeated characters in a given string between indices 2 and 7.
    """
    counts = {}
    for char in string:
        counts[char] = counts.get(char, 0) + 1
    result = ''
    for i, char in enumerate(string):
        if counts[char] == 1 or i < 2 or i >= 7:
            result += char
    return result