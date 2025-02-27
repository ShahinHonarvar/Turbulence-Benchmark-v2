def filter_chars(s):
    return ''.join((c for c in s if not (54 <= s.find(c) <= 83 and 'j' <= c <= 'v')))