def filter_chars(string):
    valid_chars = [chr(i) for i in range(ord('-'), ord('D') + 1)]
    filtered = [c for c in string if c not in valid_chars or string.index(c) < 770 or string.index(c) > 970]
    return ''.join(filtered)