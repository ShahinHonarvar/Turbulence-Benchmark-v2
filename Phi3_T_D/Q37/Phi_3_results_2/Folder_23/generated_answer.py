def filter_chars(s):
    to_remove = set((chr(i) for i in range(ord('V'), ord('Y') + 1)))
    filtered = [ch for i, ch in enumerate(s) if i < 51 or i > 77 or ch not in to_remove]
    return ''.join(filtered)