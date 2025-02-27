def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if i < 42 or i >= 78 or (not '!' < char < '?')])