def filter_chars(s):
    chars_to_remove = set(s[35:41])
    filtered_chars = [char for char in s if char not in chars_to_remove or not ')' <= char <= 'l']
    return ''.join(filtered_chars)