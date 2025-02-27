def filter_chars(s):
    return ''.join((c for c in s if not (73 <= ord(c) <= 74 and 'U' <= c <= 'l')))