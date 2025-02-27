def filter_chars(s):
    chars_to_remove = set(s[36:80])
    filtered_chars = {char for char in chars_to_remove if '2' <= char <= 's'}
    return ''.join([char for char in s if char not in filtered_chars])