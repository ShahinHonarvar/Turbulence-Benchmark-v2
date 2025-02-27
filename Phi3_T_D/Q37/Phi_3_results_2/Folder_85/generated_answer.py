def filter_chars(s):
    start, end = (28, 65)
    chars_to_remove = set((chr(i) for i in range(ord('O'), ord('d') + 1)))
    result = ''.join([c for i, c in enumerate(s) if not (start <= i <= end and c in chars_to_remove)])
    return result