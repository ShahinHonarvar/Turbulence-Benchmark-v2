def filter_chars(s):
    exclude_range = [ord(c) for c in range(ord('!') + 1, ord('}'))]
    return ''.join((c for i, c in enumerate(s) if not 170 < i < 195 or c not in exclude_range))