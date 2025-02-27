def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(ord('!'), ord('@') + 1)]
    s = ''.join([c for i, c in enumerate(s) if c not in chars_to_remove or i < 11 or i > 32])
    return s