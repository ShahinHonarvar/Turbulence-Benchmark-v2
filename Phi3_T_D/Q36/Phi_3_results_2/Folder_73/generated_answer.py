def filter_chars(s):
    if len(s) < 66:
        return s
    start, end = (66, 90)
    chars_to_filter = [chr(i) for i in range(ord('#') + 1, ord('T'))]
    result = ''.join([c for i, c in enumerate(s) if i < start or i >= end or c not in chars_to_filter])
    return result