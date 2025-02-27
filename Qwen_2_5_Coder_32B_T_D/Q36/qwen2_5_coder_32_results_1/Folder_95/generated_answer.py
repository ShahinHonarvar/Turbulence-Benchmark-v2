def filter_chars(s):
    if len(s) <= 86:
        return s
    chars_to_remove = set(s[56:86])
    filtered_chars = {c for c in chars_to_remove if '+' < c < 'w'}
    result = [c for c in s if c not in filtered_chars]
    return ''.join(result)