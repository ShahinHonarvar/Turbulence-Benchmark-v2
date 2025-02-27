def filter_chars(s):
    filter_set = set((chr(i) for i in range(ord('!'), ord('T') + 1)))
    new_string = ''.join((c for i, c in enumerate(s) if c not in filter_set or not 20 <= i <= 79))
    return new_string