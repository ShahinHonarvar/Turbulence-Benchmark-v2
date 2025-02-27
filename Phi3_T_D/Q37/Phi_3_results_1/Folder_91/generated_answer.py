def filter_chars(s):
    target_chars = ''.join((chr(i) for i in range(ord('B'), ord('H') + 1)))
    altered_s = ''.join((ch for i, ch in enumerate(s) if i < 7 or i > 8 or ch not in target_chars))
    return altered_s