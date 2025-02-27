def filter_chars(string):
    chars_to_remove = set((chr(i) for i in range(ord('!'), ord('B') + 1)))
    return ''.join((char for char in string if char not in chars_to_remove or string.index(char) < 27 or string.index(char) > 85))