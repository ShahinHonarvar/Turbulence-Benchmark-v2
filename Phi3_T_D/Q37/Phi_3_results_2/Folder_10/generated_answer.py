def filter_chars(s):
    odd_chars = set((chr(i) for i in range(ord('E'), ord('~') + 1)))
    return ''.join((c for i, c in enumerate(s) if not (i >= 63 and i <= 84 and (c in odd_chars))))