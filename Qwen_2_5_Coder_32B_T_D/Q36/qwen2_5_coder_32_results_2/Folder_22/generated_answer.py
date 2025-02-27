def filter_chars(s):
    chars_to_remove = set(s[55:84])
    filtered_chars = {char for char in chars_to_remove if ';' < char < 'z'}
    return ''.join((char for char in s if char not in filtered_chars))