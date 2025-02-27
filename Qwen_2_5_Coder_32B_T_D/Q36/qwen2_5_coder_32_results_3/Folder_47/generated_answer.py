def filter_chars(s):
    chars_to_remove = set(s[45:57])
    filtered_chars = {char for char in chars_to_remove if 'F' < char < 'n'}
    return ''.join((char for char in s if char not in filtered_chars))