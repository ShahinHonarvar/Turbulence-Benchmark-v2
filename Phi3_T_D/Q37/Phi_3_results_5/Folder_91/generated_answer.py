def filter_chars(s):
    target_char = s[7]
    return ''.join((c for i, c in enumerate(s) if not (i == 7 and c == target_char) or not 'B' <= c <= 'H'))