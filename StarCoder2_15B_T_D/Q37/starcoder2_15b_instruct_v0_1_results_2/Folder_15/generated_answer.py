def filter_chars(string):
    """
    Filter characters between indices 2 and 6 (inclusive) and in the range '?' to 'f' from a string.
    """
    result = []
    for i, c in enumerate(string):
        if 2 <= i <= 6 and '?' <= c <= 'f':
            continue
        result.append(c)
    return ''.join(result)