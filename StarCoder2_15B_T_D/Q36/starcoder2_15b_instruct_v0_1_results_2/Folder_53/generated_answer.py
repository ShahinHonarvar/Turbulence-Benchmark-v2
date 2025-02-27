def filter_chars(string):
    return ''.join((c for i, c in enumerate(string) if i < 90 or i >= 97 or c <= 'j' or (c >= 'w')))