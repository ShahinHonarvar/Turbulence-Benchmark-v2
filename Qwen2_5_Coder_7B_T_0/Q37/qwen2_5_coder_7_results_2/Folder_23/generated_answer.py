def filter_chars(s):
    return ''.join((c for c in s if not (51 <= s.index(c) <= 77 and 'V' <= c <= 'Y')))