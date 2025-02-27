def filter_chars(s):
    return ''.join((c for i, c in enumerate(s, start=1) if not (72 <= i <= 94 and ord('.') <= ord(c) <= ord('b'))))