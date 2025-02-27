def filter_chars(s):
    return ''.join((c for c in s if (c < '<' or c > 'w') or 57 <= s.index(c) <= 96))