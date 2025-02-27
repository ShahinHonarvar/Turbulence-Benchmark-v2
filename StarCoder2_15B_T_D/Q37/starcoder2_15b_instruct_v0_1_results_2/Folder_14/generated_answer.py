def filter_chars(s):
    """
    Filters characters from a string `s` according to the given conditions.
    """
    chars_to_remove = {c for c in s[35:99] if 'A' <= c <= 'b'}
    filtered_chars = [c for c in s if c not in chars_to_remove]
    return ''.join(filtered_chars)