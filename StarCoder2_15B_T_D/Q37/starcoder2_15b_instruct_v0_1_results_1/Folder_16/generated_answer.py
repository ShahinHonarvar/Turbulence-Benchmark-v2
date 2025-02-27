def filter_chars(string):
    chars_to_remove = set((chr(i) for i in range(ord('D'), ord('Z') + 1) if 225 <= i <= 381))
    return ''.join((c for c in string if c not in chars_to_remove))