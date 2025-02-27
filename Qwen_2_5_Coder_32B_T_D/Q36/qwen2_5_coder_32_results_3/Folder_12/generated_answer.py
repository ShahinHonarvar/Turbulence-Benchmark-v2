def filter_chars(s):
    return ''.join((c for c in s if ord(c) < 32 or ord(c) > 84 or (not 'm' < c < 'w')))