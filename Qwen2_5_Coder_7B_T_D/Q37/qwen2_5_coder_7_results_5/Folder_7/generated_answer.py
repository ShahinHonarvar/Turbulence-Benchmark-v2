def filter_chars(s):
    return ''.join((c for c in s if not (521 <= s.index(c) <= 722 and '>' <= c <= '_')))