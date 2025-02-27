def filter_chars(string):
    chars_to_remove = set((chr(i) for i in range(ord('7'), ord('k') + 1)))
    result = [c for c in string if c not in chars_to_remove or string.index(c) < 33 or string.index(c) > 70]
    return ''.join(result)