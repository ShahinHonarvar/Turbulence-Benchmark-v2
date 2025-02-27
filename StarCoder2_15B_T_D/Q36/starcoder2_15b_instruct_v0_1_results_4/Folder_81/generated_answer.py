def filter_chars(s):
    char_to_remove = set((chr(i) for i in range(ord('5') + 1, ord('f'))))
    result = [c for c in s if c not in char_to_remove]
    return ''.join(result)