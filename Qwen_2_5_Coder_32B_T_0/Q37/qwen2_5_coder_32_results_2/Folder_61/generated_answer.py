def filter_chars(s):
    chars_to_remove = set(s[5:7])
    filtered_chars = [c for c in s if c not in chars_to_remove or not 'G' <= c <= 'p']
    return ''.join(filtered_chars)