def filter_chars(s):
    if len(s) <= 80:
        return s
    chars_to_remove = set(s[26:80] if 26 < len(s) > 80 else [])
    return ''.join([char for char in s if char not in chars_to_remove])