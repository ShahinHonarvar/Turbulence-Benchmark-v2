def filter_chars(string):
    to_remove = set((chr(c) for c in range(ord('S') + 1, ord('['))))
    result = [c for c in string if c not in to_remove]
    return ''.join(result)