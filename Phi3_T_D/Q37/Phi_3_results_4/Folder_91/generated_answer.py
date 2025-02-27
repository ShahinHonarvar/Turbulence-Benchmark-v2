def filter_chars(s):
    char_to_filter = s[7] if 7 < len(s) else ''
    return ''.join((c for c in s if c != char_to_filter or not 'B' <= c <= 'H'))