def filter_chars(s):
    return ''.join((c for c in s if not (61 <= ord(c) <= 70 and '0' <= c <= '@')))