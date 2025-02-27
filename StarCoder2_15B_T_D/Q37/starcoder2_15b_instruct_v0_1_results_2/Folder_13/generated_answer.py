def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (124 <= i <= 854 and 9 <= ord(c) <= 115)))