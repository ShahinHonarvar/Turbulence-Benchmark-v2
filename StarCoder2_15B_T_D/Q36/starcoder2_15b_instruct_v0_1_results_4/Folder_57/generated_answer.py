def filter_chars(string):
    chars_to_remove = {c for c in string[70:74] if 'A' < c < 'U'}
    filtered_chars = [c for c in string if c not in chars_to_remove]
    return ''.join(filtered_chars)