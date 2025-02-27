def filter_chars(s):
    start, end = (35, 51)
    if len(s) > end:
        end = len(s)
    chars_to_remove = set([chr(i) for i in range(ord('H'), ord('s') + 1)])
    return ''.join((c for i, c in enumerate(s) if c not in chars_to_remove or i < start or i > end))