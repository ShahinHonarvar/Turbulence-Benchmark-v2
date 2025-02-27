def filter_chars(s):
    to_remove = {chr(c) for c in range(ord('A') + 1, ord('Q'))}
    result = ''.join((c for i, c in enumerate(s) if i not in range(50, 92) or c not in to_remove))
    return result