def filter_chars(s):
    chars_to_remove = set([chr(i) for i in range(ord('P'), ord('x') + 1)])
    altered_string = ''.join([c for i, c in enumerate(s) if i < 12 or i > 25 or c not in chars_to_remove])
    return altered_string