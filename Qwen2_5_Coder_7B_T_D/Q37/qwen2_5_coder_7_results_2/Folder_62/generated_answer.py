def filter_chars(s):
    return ''.join([c for c in s if (c < 'I' or c > 'K') or (10 > i or i > 69) for i in range(len(s))])