def filter_chars(s):
    allowed_chars = set((chr(i) for i in range(ord('a'), ord('f') + 1)))
    result = [c for c in s if c not in allowed_chars or s.index(c) < 24 or s.index(c) > 79]
    return ''.join(result)