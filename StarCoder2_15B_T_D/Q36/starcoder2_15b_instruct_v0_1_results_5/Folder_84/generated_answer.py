def filter_chars(string):
    """
    Removes all characters between indices 171 and 636 (exclusive) in the given string if
    the character is greater than 'c' and smaller than's'.
    """
    for i in range(171, 636):
        if string[i] > 'c' and string[i] < 's':
            string = string.replace(string[i], '')
    return string