def filter_chars(s):
    target_chars = [chr(i) for i in range(ord('8'), ord('e') + 1)]
    s = ''.join([c for i, c in enumerate(s) if not (75 <= i <= 99 and c in target_chars)])
    return s