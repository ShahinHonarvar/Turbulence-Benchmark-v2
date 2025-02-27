def filter_chars(s):
    target_range = set((chr(i) for i in range(ord('O'), ord('}') + 1)))
    return ''.join((c for i, c in enumerate(s) if not (164 <= i <= 706 and c in target_range)))