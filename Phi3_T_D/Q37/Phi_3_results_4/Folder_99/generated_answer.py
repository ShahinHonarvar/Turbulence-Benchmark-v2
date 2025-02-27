def filter_chars(s):
    accept_chr = set((chr(i) for i in range(ord('T'), ord('h') + 1)))
    return ''.join((c for i, c in enumerate(s) if i < 373 or i > 901 or c not in accept_chr))