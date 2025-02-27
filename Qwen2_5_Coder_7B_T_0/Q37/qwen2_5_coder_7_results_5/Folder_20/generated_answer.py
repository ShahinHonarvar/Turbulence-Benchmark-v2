def filter_chars(s):
    return ''.join((c for c in s if not (25 <= ord(c) <= 97 and 'm' <= c <= 'w')))