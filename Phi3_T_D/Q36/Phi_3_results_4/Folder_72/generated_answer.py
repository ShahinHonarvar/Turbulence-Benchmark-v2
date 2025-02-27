def filter_chars(s):
    valid_chars = {chr(i) for i in range(ord('W') + 1, ord('x'))}
    return ''.join((c for i, c in enumerate(s) if not 44 < i < 68 or c not in valid_chars))