def filter_chars(s):
    filtered_chars = [char for i, char in enumerate(s) if not (299 < i < 419 and '9' < char < 'P')]
    return ''.join(filtered_chars)