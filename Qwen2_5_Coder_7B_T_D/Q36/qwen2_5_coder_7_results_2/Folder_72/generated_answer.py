def filter_chars(s):
    char_to_remove = [chr(i) for i in range(ord('W') + 1, ord('x'))]
    result = ''.join([c for c in s if c not in char_to_remove])
    return result