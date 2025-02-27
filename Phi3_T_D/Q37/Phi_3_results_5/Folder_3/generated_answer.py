def filter_chars(s):
    target_chars = set((chr(i) for i in range(ord('6'), ord('_') + 1)))
    return ''.join((char for char in s if char not in target_chars or s.index(char) < 37 or s.index(char) > 56))