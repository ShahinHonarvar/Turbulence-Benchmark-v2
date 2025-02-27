def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(ord('f') + 1, ord('|'))]
    altered_string = ''.join([c for i, c in enumerate(s) if i not in range(55, 66) or c not in chars_to_remove])
    return altered_string