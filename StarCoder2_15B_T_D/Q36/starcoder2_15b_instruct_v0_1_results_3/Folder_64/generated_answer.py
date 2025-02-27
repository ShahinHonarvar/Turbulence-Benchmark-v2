def filter_chars(text: str) -> str:
    """
    For each character between the indices 1 and 7 (both exclusive) in the given string,
    if that character is greater than character '3' and smaller than character '^',
    remove all occurrences of that character within the string while keeping the order
    of all characters in the string intact.
    """
    result = ''
    for i, c in enumerate(text):
        if i < 1 or i >= 7:
            result += c
        elif not (ord(c) > ord('3') and ord(c) < ord('^')):
            result += c
    return result