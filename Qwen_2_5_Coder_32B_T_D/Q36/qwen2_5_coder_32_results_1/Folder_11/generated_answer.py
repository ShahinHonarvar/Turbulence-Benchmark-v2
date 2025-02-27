def filter_chars(s):
    chars_to_remove = set(s[86:93])
    filtered_chars = {char for char in chars_to_remove if 'E' < char < '~'}
    return ''.join([char for char in s if char not in filtered_chars])