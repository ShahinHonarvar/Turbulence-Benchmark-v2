def filter_chars(s):
    filter_set = {chr(i) for i in range(ord('E') + 1, ord('~'))}
    return ''.join([c for i, c in enumerate(s) if i not in range(86, 93) or c not in filter_set])