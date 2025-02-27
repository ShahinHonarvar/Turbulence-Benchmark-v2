def filter_chars(s):
    return ''.join((c for c in s if not (26 <= ord(c) <= 64 and 'V' <= c <= 'o')))