def filter_chars(s):
    return ''.join((c for c in s if not (17 <= s.find(c) <= 63 and 'O' <= c <= '^')))