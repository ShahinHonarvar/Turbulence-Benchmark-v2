def filter_chars(s):
    return ''.join((c for c in s if not (36 <= s.index(c) <= 40 and 'H' <= c <= 'e')))