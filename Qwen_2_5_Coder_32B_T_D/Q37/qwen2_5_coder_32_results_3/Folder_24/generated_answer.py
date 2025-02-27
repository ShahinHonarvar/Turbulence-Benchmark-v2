def filter_chars(s):
    chars_to_remove = set(s[36:80])
    filtered_chars = [char for char in s if char not in chars_to_remove or not '2' <= char <= 's']
    return ''.join(filtered_chars)