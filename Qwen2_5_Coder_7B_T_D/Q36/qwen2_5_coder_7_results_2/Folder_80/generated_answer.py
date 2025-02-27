def filter_chars(s):
    return s[:54] + ''.join((c for c in s[92:] if not (c > 'J' and c < 'X')))