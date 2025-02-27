def filter_chars(s):
    chrs = set((chr(i) for i in range(ord('-'), ord('D') + 1)))
    altered = [c for i, c in enumerate(s) if i not in range(770, 971) or c not in chrs]
    return ''.join(altered)