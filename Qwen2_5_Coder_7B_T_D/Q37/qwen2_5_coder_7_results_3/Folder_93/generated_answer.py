def filter_chars(s):
    return ''.join((c for c in s if not (38 <= s.index(c) <= 69 and 'H' <= c <= 'e')))