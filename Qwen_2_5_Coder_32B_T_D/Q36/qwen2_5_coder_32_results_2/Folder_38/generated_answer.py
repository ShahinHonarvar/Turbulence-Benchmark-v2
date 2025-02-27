def filter_chars(s):
    chars_to_remove = set(s[45:47])
    filtered_chars = [c for c in s if c not in chars_to_remove or not '+' < c < 'l']
    return ''.join(filtered_chars)