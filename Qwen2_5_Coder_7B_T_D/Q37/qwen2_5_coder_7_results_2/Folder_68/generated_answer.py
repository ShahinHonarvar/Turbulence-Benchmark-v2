def filter_chars(s):
    to_remove = {chr(i) for i in range(ord('6'), ord('w') + 1)}
    return ''.join((c for i, c in enumerate(s) if i < 7 or i > 9 or c not in to_remove))