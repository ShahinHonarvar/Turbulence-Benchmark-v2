def filter_chars(s):
    chars_to_remove = set(s[22:25])
    filtered_chars = {char for char in chars_to_remove if '5' < char < '}'}
    return ''.join((char for char in s if char not in filtered_chars))