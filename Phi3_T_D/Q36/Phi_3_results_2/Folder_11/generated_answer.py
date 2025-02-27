def filter_chars(s):
    if not s or len(s) <= 93:
        return s
    modified_chars = [c for c in s[:86] + s[93:] if c <= 'E' or c >= '~']
    return ''.join(modified_chars)