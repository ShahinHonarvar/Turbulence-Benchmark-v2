def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (27 <= i <= 85 and ord('!') <= ord(c) <= ord('B'))))