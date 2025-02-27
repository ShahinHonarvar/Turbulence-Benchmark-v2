def filter_chars(s):
    chars_to_remove = set(';:<=>?@')
    return ''.join((c for i, c in enumerate(s) if not (31 <= i <= 38 and c in chars_to_remove)))