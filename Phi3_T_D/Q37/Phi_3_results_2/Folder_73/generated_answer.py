def filter_chars(s):
    target_chars = set((chr(i) for i in range(ord('7'), ord('e') + 1)))
    return ''.join((c for idx, c in enumerate(s) if c not in target_chars or not 22 <= idx <= 85))