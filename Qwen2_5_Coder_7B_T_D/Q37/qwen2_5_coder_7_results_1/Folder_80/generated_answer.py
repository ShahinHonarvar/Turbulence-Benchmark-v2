def filter_chars(s):
    bad_chars = {chr(i) for i in range(ord('a'), ord('i') + 1)}
    return ''.join((ch for i, ch in enumerate(s) if i < 36 or i > 79 or ch not in bad_chars))