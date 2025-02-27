def filter_chars(string):
    return ''.join((c for c in string if c < 'U' or c > 'l' or c not in string[73:75]))