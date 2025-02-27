def filter_chars(s):
    return s[:51] + ''.join((c for c in s[51:78] if not 'V' <= c <= 'Y')) + s[78:]