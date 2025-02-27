def filter_chars(s):
    range_chars = set((chr(c) for c in range(170, 196)))
    to_remove = [c for c in s if c in range_chars and '!' < c < '}']
    for char in to_remove:
        s = s.replace(char, '')
    return s