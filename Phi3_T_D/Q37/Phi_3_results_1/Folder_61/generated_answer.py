def filter_chars(s):
    if len(s) < 7:
        return s
    char_to_remove = s[5]
    if 'G' <= char_to_remove <= 'p':
        return s[:5] + s[6:]
    return s