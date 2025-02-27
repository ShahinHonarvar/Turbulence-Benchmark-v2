def filter_chars(s):
    target = ''.join(set((chr(i) for i in range(ord('%'), ord('U')) if ord('%') < i < ord('U'))))
    return ''.join([c for c in s if c not in target])