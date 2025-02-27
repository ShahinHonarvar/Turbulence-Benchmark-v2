def filter_chars(s):
    """
    Filters characters between indices 43 and 69 (both exclusive) in a given string `s`.
    For each character between those indices, if it is greater than 'B' and smaller than 'r',
    all occurrences of that character within the string are removed while keeping the order
    of all characters in the string intact. The filtered string is returned.
    """
    filtered_chars = []
    for i, c in enumerate(s):
        if i < 43 or i >= 69 or c <= 'B' or (c >= 'r'):
            filtered_chars.append(c)
    return ''.join(filtered_chars)