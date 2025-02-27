def filter_chars(s):
    start, end = (24, 79)
    allowed_chars = {chr(i) for i in range(ord('a'), ord('f') + 1)}
    return ''.join((char for i, char in enumerate(s) if i < start or i > end or char not in allowed_chars))