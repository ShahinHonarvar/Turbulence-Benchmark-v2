def filter_chars(s):
    to_remove = (chr(i) for i in range(ord('t'), ord('v')))
    return ''.join((c for i, c in enumerate(s) if not 10 < i < 15 or c not in to_remove))