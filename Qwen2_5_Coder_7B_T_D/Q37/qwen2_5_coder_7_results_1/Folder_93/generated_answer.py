def filter_chars(s):
    return ''.join((c for c in s if not (38 <= s.find(c) <= 69 and 'H' <= c <= 'e')))