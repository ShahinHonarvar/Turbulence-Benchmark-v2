def filter_chars(s):
    to_remove = set([chr(i) for i in range(ord('P'), ord('x') + 1)])
    return ''.join([c for i, c in enumerate(s) if i < 12 or i > 25 or c not in to_remove])