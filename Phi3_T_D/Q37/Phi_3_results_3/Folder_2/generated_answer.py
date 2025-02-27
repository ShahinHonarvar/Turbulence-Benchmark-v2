def filter_chars(s):
    start_idx = 477
    end_idx = 984
    char_to_remove = set((chr(i) for i in range(ord(','), ord('V') + 1)))
    return ''.join((c for i, c in enumerate(s) if i < start_idx or i > end_idx or c not in char_to_remove))