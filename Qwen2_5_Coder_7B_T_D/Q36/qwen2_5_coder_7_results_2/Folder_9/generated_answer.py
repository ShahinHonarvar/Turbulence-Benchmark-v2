def filter_chars(s):
    return ''.join(filter(lambda x: x <= 'A' or x >= 'Q', s))