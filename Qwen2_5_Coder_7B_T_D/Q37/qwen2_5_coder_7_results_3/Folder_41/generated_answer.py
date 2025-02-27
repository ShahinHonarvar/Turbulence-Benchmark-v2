def filter_chars(s):
    return ''.join((c for c in s if not ('V' <= c <= 'o' and 26 <= ord(c) <= 64)))