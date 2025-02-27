def filter_chars(s):
    start = 138
    end = 920
    target_range = set((chr(i) for i in range(ord('6'), ord('A') + 1)))
    return ''.join((c for i, c in enumerate(s) if i < start or i > end or c not in target_range))