def filter_chars(s):
    return ''.join((c for c in s if 52 <= ord(c) < 88 and (not '&' < c < 'c')))