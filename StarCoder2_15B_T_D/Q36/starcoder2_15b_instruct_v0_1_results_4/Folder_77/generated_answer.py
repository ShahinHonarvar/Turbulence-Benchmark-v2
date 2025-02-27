def filter_chars(string):
    """
    Filter characters between indices 221 and 419 in the given string.
    """
    filtered_chars = [char for i, char in enumerate(string) if i < 221 or i >= 419 or (not '-' < char < 'v')]
    return ''.join(filtered_chars)