def filter_chars(s):
    return ''.join((c for c in s if not (90 < ord(c) < 97 and 'j' < c < 'w')))