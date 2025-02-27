def filter_chars(s):
    chars_to_remove = set(s[46:68])
    filtered_chars = {char for char in chars_to_remove if 'H' < char < 's'}
    return ''.join([char for char in s if char not in filtered_chars])