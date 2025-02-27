def filter_chars(s):
    return ''.join((c for c in s if not (51 <= s.find(c) <= 96 and 'X' <= c <= 'p')))