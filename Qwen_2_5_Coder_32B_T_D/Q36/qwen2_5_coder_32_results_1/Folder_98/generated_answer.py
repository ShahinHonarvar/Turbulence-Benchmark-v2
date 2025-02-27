def filter_chars(s):
    chars_to_remove = set(s[5:8])
    filtered_chars = {char for char in chars_to_remove if '1' < char < 'J'}
    return ''.join([char for char in s if char not in filtered_chars])