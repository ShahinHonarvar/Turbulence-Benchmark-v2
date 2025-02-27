def filter_chars(string):
    forbidden_chars = set((chr(i) for i in range(ord('B') + 1, ord('Y'))))
    filtered_string = ''.join((c for c in string if c not in forbidden_chars))
    return filtered_string