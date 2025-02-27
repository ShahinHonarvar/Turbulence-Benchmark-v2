def filter_chars(s):
    filter_set = set((chr(i) for i in range(ord(';') + 1, ord('z'))))
    return ''.join((char for char in s if char not in filter_set))