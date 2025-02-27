def filter_chars(string):
    chars_to_remove = set((chr(i) for i in range(ord('f') + 1, ord('~'))))
    return ''.join((char for char in string if char not in chars_to_remove))