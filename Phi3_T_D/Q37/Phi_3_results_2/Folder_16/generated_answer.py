def filter_chars(s):
    s = ''.join((c for c in s if c < 'D' or c > 'Y' or (not 225 <= ord(c) <= 381)))
    return s