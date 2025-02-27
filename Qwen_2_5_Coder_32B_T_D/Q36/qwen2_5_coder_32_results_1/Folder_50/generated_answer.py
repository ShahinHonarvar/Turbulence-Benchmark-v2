def filter_chars(s):
    chars_to_remove = set(s[61:88])
    filtered_chars = {c for c in chars_to_remove if '%' < c < 'q'}
    result = [c for c in s if c not in filtered_chars]
    return ''.join(result)