def filter_chars(s):
    to_remove = set((chr(i) for i in range(ord('g'), ord('o'))))
    return ''.join((char for char in s if char not in to_remove))