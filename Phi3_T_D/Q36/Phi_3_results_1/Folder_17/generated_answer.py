def filter_chars(s):
    result = ''.join([c for i, c in enumerate(s) if not 18 <= i < 95 or not 'K' < c < 'a'])
    return result