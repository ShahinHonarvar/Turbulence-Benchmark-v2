def filter_chars(s):
    return ''.join((c for c in s if not (31 <= ord(c) <= 38 and ';' <= c <= 'g')))