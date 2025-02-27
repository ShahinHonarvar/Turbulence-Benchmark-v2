def filter_chars(s):
    return ''.join((c for c in s if not (c > '?' and c < 'm') or not 10 < s.index(c) < 79))