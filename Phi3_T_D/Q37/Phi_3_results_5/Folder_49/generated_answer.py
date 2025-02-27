def filter_chars(s):
    valid_chars = set('*abcdefghij')
    return ''.join([c for i, c in enumerate(s) if not (42 <= i <= 97 and c in valid_chars)])