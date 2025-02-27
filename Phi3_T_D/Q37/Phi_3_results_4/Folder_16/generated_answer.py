def filter_chars(s):
    target_chars = ''.join((chr(i) for i in range(ord('D'), ord('Y') + 1)))
    return ''.join((c for i, c in enumerate(s) if c not in target_chars or not 225 <= i <= 381))