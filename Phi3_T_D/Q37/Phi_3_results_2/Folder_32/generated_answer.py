def filter_chars(s):
    return ''.join([char for i, char in enumerate(s) if i < 23 or i > 89 or char < 'w' or (char > '{')])