def filter_chars(string):
    """
    Filter characters between indices 1 and 9 (exclusive) in a given string.
    For each character between indices 1 and 9 (both exclusive) in the given string,
    if the character is greater than '8' and smaller than'm', remove all occurrences
    of that character within the string while keeping the order of all characters intact.
    """
    filtered_string = ''
    for i, char in enumerate(string):
        if i > 0 and i < 9 and (char > '8') and (char < 'm'):
            continue
        filtered_string += char
    return filtered_string