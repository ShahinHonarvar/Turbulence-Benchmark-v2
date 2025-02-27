def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(ord('5') + 1, ord('C'))]
    return ''.join((c for i, c in enumerate(s) if i < 43 or i >= 59 or c not in chars_to_remove))