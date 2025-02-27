def filter_chars(s):
    return ''.join((c for c in s if not (82 < ord(c) < 89 and '*' < c < '[')))