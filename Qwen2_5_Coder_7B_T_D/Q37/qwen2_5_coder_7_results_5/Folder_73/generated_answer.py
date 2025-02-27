def filter_chars(s):
    chars_to_remove = set('789abcde')
    return ''.join((c for i, c in enumerate(s) if not (22 <= i <= 85 and c in chars_to_remove)))