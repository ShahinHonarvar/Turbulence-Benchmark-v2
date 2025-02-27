def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('A') + 1, ord('U'))}
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result