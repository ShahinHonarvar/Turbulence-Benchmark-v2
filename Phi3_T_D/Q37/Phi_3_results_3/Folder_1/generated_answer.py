def filter_chars(s):
    start, end = (41, 79)
    chars_to_remove = {chr(i) for i in range(ord('f'), ord('|') + 1)}
    altered = [c for i, c in enumerate(s) if i < start or i > end or c not in chars_to_remove]
    return ''.join(altered)