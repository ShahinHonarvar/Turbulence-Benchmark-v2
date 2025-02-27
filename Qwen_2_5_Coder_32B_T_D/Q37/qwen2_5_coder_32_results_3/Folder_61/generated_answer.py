def filter_chars(s):
    chars_to_remove = set(s[5:7])
    filtered_chars = [char for char in s if char not in chars_to_remove or not 'G' <= char <= 'p']
    return ''.join(filtered_chars)