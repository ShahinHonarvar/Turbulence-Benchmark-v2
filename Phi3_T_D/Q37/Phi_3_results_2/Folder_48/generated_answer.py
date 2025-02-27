def filter_chars(s):
    target_chars = [chr(i) for i in range(ord('?'), ord('n') + 1)]
    return ''.join((c for i, c in enumerate(s) if c not in target_chars or not 513 <= i <= 877))