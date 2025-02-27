def filter_chars(s):
    to_remove = {chr(i) for i in range(ord('H'), ord('e') + 1)}
    return ''.join((c for c in s if c not in to_remove))